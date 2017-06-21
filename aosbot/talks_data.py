import yaml


# Talk types: session, general, break, extra

# emoji: :coffee::alarm_clock::watch::hourglass_flowing_sand:
# :calendar::fork_and_knife::raising_hand::footprints:
# :speech_balloon::thought_balloon:
# :pig::pig_nose::ghost::gift:
# :closed_book::blue_book::orange_book::notebook::space_invader:


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
