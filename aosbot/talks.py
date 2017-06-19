import dateutil.parser
import yaml


talks_data = yaml.safe_load("""
---

talks:
  - from_time: "2017-06-20T10:00:00+0200"
    to_time: "2017-06-20T11:00:00+0200"
    room: Auditorio
    title: Charla número 1
    description: |
        Esta charla
        es una charla de prueba
  - from_time: "2017-06-20T10:00:00+0200"
    to_time: "2017-06-20T11:00:00+0200"
    room: Aula
    title: Charla número 2
    description: |
        Esta charla
        es una charla de prueba
  - from_time: "2017-06-20T11:00:00+0200"
    to_time: "2017-06-20T12:00:00+0200"
    room: Auditorio
    title: Charla número 3
    description: |
        Esta charla
        es una charla de prueba

  - from_time: "2017-06-20T11:00:00+0200"
    to_time: "2017-06-20T12:00:00+0200"
    room: Aula
    title: Charla número 4
    description: |
        Esta charla
        es una charla de prueba

""")


class Talk:
    def __init__(self,from_time, to_time, room, title, description):
        self.from_time = dateutil.parser.parse(from_time)
        self.to_time = dateutil.parser.parse(to_time)
        self.room = room
        self.title = title
        self.description = description

    def is_now(self, time):
        return self.from_time <= time < self.to_time

    def is_passed(self, time):
        return time > self.to_time

    def is_upcoming(self, time):
        return self.from_time >= time

    def __lt__(self, other):
        if self.from_time == other.from_time:
            return self.room < other.room
        else:
            return self.from_time <= other.from_time

    def __str__(self):
        return "\n".join([
            f"*·* {self.from_time:%H:%M}-{self.to_time:%H:%M} _{self.room}_",
            f"*{self.title}*",
            f"{self.description}",
        ])


talks_data = [Talk(**t) for t in talks_data["talks"]]
