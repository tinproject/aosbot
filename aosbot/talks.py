import dateutil.parser
from .talks_data import talks_data, get_emoji


class Talk:
    def __init__(self, session_type, from_time, to_time, room, icon, title, proposer, description):
        self.session_type = session_type
        self.from_time = dateutil.parser.parse(from_time)
        self.to_time = dateutil.parser.parse(to_time)
        self.room = room
        self.icon = icon
        self.title = title
        self.proposer = proposer
        self.description = description

    def is_now(self, time):
        return self.from_time <= time < self.to_time

    def is_passed(self, time):
        return time > self.to_time

    def is_upcoming(self, time):
        return self.from_time >= time

    def is_talk(self):
        return self.session_type == "session"

    def is_break(self):
        return self.session_type == "break"

    def __lt__(self, other):
        if self.from_time == other.from_time:
            return self.room < other.room
        else:
            return self.from_time <= other.from_time

    def __str__(self):
        text = {
            "break": "\n".join([
                f"{get_emoji(self.icon)} {self.from_time:%H:%M} - {self.to_time:%H:%M}",
                f"*{self.title}*",
                ""
            ]),
            "extra": "\n".join([
                f"{get_emoji(self.icon)} {self.from_time:%H:%M} - {self.to_time:%H:%M} _{self.room}_",
                f"*{self.title}*",
                f"Facilitada por: {self.proposer}",
                f"{self.description}",
            ]),
            "general": "\n".join([
                f"{get_emoji(self.icon)} {self.from_time:%H:%M} - {self.to_time:%H:%M} _{self.room}_",
                f"*{self.title}*",
                f"{self.description}",
            ]),
            "session": "\n".join([
                f"{get_emoji(self.icon)} {self.from_time:%H:%M} - {self.to_time:%H:%M} _{self.room}_",
                f"*{self.title}*",
                f"Propuesta por: {self.proposer}",
                ""
            ]),
        }

        return text[self.session_type]


class TalkManager:
    def __init__(self, talks_data):
        self.talks = [Talk(**t) for t in talks_data["talks"]]

    def get_now_talks(self, time):
        return [t for t in self.talks if t.is_now(time)]

    def get_next_talks(self, time):
        return [t for t in self.talks if t.is_upcoming(time) and t.is_talk()]

    def get_all_talks(self):
        return self.talks


talk_manager = TalkManager(talks_data)
