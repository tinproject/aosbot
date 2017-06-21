import dateutil.parser
import yaml


# Talk types: session, general, break, extra

talks_data = yaml.safe_load("""
---

talks:
  # - session_type: session
  #   from_time: "2017-06-24T09:00:00+0200"
  #   to_time: "2017-06-24T10:00:00+0200"
  #   room: 
  #   title:
  #   proposer:
  #   description:

# Viernes 23

  - session_type: extra
    from_time: "2017-06-23T11:00:00+0200"
    to_time: "2017-06-23T13:00:00+0200"
    room: Campus María Zambrano
    title: Let's Play Agile Games
    proposer: Amalia Hernández y Delia Estebaranz
    description: |
        Juegos acerca de la formación de equipos y la confianza. 
        Apto para todo tipo de públicos.

  - session_type: extra
    from_time: "2017-06-23T11:00:00+0200"
    to_time: "2017-06-23T13:00:00+0200"
    room: Campus María Zambrano
    title: AOS Code Jam
    proposer: José Dova y Agustín Herranz
    description: |
        Sesión abierta sobre programación en la que practicar, plantear dudas, enseñar código, debatir... 
        podrás traer tu portátil para trabajar sobre código y aprender un montón de cosas..

  - session_type: general
    from_time: "2017-06-23T16:00:00+0200"
    to_time: "2017-06-23T17:30:00+0200"
    room: Campus María Zambrano
    title: Apertura del AOS 2017
    proposer: AOS
    description: |
        ¿En qué consiste el AOS 2017?
        Presentación y actividades previas.

  - session_type: general
    from_time: "2017-06-23T17:30:00+0200"
    to_time: "2017-06-23T19:30:00+0200"
    room: Campus María Zambrano
    title: Creación del panel y votación de las sesiones.
    proposer: AOS
    description: |
        Las personas que lo deseen proponen una sesión o un tema del que hablar explicando brevemente el contenido y enfoque de la sesión.
        Tras proponer todas las sesiones, los asistentes votan aquellas que sean de su interés.
        Las más votadas se repartirán en el panel final estableciendo la agenda del sábado.

# Sábado 24

  - session_type: general
    from_time: "2017-06-24T09:00:00+0200"
    to_time: "2017-06-24T10:00:00+0200"
    room: 
    title: Apertura de las sesiones
    proposer: AOS
    description:

  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: room
    title: Session I
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: room
    title: Session II
    proposer: AOS
    description: ...

  - session_type: break
    from_time: "2017-06-24T12:00:00+0200"
    to_time: "2017-06-24T12:30:00+0200"
    room: room
    title: Coffe break
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: room
    title: Session III
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: room
    title: Session IV
    proposer: AOS
    description: ...

  - session_type: break
    from_time: "2017-06-24T14:30:00+0200"
    to_time: "2017-06-24T16:00:00+0200"
    room: room
    title: Comida
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: room
    title: Session V
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: room
    title: Session VI
    proposer: AOS
    description: ...

  - session_type: general
    from_time: "2017-06-24T18:00:00+0200"
    to_time: "2017-06-24T19:00:00+0200"
    room: 
    title: Retrospectiva y cierre AOS 2017
    proposer: AOS
    description:

""")  # NoQA E501, W291


class Talk:
    def __init__(self, session_type, from_time, to_time, room, title, proposer, description):
        self.session_type = session_type
        self.from_time = dateutil.parser.parse(from_time)
        self.to_time = dateutil.parser.parse(to_time)
        self.room = room
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
        return "\n".join([
            f"*·* {self.from_time:%H:%M} - {self.to_time:%H:%M} _{self.room}_",
            f"*{self.title}*",
            f"Propuesta por: {self.proposer}"
            f"{self.description}",
        ])


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
