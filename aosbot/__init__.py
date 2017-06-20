import datetime as dt
import logging
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from .tg.update_handler import UpdateHandler  # NoQA E402
from .tg.api_types import Message  # NoQA E402
from . import config  # NoQA E402
from .talks import talks_data  # NoQA E402


COMMAND_BOT_REGEX = r"^/(?P<command>[a-zA-Z0-9_]{1,31})(?:@(?P<bot_username>[a-zA-Z0-9_]{5,32}))?"


def generate_error_response(error, error_code=400, error_message=""):
    error_message = {
        "error": error,
        "error_code": error_code,
        "error_message": error_message,
    }
    return error_message


def send_message_in_response(chat_id, text,
                             parse_mode="Markdown",
                             disable_web_page_preview=True,
                             disable_notification=False,
                             reply_to_message_id=None,
                             ):
    response = {
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": disable_web_page_preview,
        "disable_notification": disable_notification,
    }
    if reply_to_message_id is not None:
        response["reply_to_message_id"] = reply_to_message_id
    return response


def not_implemented_handler(message_dict):
    return generate_error_response("NOT IMPLEMENTED", 500)


def command_handler_start(Message):
    return "\n".join([
        f"Hola, soy *{config.BOT_NAME}* y estoy aquí para ayudarte a que "
        "no te pierdas ninguna sesión interesante del AOS 2017 en Segovia.",
        "Soy un bot muy _funcional_ y _carezco de estado_. Como no tengo memoria, "
        "solo puedo responderte más cosas para las que me han programado. "
        "Puedes ver mis tripas en [Github](https://github.com/tinproject/aosbot).",
        "Si quieres algo de mí, has de hablarme mediante comandos, por ejemplo, "
        "si me pides */ayuda* te dire cual es el listado de comandos disponibles.",
    ])


def command_handler_help(Message):
    return "\n".join([
        "Estos son los comandos a los que respondo:",
        "*/ayuda* - Esta ayuda es que estás leyendo.",
        "*/ahora* - Te cuento las sesiones que hay en este mismo instante.",
        "*/siguientes* - Las que empezarán dentro de un rato.",
        "*/programa* - Todas las sesiones que hay programadas."
    ])


def command_handler_ahora(Message):
    now = dt.datetime.now(dt.timezone.utc)
    talks = [t for t in talks_data if t.is_now(now)]
    if talks:
        response = "\n".join((str(t) for t in talks))
    else:
        response = f"Ahora mismo no hay ninguna charla."
    return response


def command_handler_siguientes(Message):
    now = dt.datetime.now(dt.timezone.utc)
    talks = [t for t in talks_data if t.is_upcoming(now)]
    if talks:
        response = "\n".join((str(t) for t in sorted(talks)))
    else:
        response = f"Ahora mismo no hay ninguna charla."
    return response


def command_handler_programa(Message):
    now = dt.datetime.now(dt.timezone.utc)
    talks = [t for t in talks_data if not t.is_passed(now)]
    if talks:
        response = "\n".join((str(t) for t in sorted(talks)))
    else:
        response = f"Ahora mismo no hay ninguna charla en el programa."
    return response


COMMAND_HANDLERS = {
    "start": command_handler_start,
    "help": command_handler_help,
    "ayuda": command_handler_help,
    "ahora": command_handler_ahora,
    "siguientes": command_handler_siguientes,
    "programa": command_handler_programa,
}


def message_handler(message_dict):
    message = Message(message_dict)

    # Is a command?
    if str.startswith(message.text, '/'):
        command, at_bot = re.match(COMMAND_BOT_REGEX, message.text).groups()
        if at_bot is not None and at_bot != config.BOT_USERNAME:
            # Commmand for ohter bot
            return generate_error_response("NOT PROCESSED", 200, f"Command for other bot {at_bot}")
        else:
            if message.chat.type == "channels":
                # Not asnwer to messages from channels
                return generate_error_response("NOT PROCESSED", 200, f"Only answer in private")

            # Process command
            if command not in COMMAND_HANDLERS:
                return generate_error_response("NOT PROCESSED", 200,
                                               f"Command not understanded {command}")
            response_text = COMMAND_HANDLERS[command](message)
            return send_message_in_response(message.chat.id, response_text)

    # It'a a message to the bot.
    return generate_error_response("NOT PROCESSED", 200, f"Not processing messages")


update_handler = UpdateHandler(
    message=message_handler,
    edited_message=not_implemented_handler,
    channel_post=not_implemented_handler,
    edited_channel_post=not_implemented_handler,
    inline_query=not_implemented_handler,
    chosen_inline_result=not_implemented_handler,
    callback_query=not_implemented_handler,
    shipping_query=not_implemented_handler,
    pre_checkout_query=not_implemented_handler,
)


def telegram_webhook_handler(event: dict, context: dict) -> dict:
    """ This function process the endpoint for the webhook handler """

    if not isinstance(event, dict):
        # Telegram objects are JSON objects so we are only receiving dicts
        # Any other input type supported by Lambda has no sense here
        logger.error("BAD REQUEST: %s", event)
        return generate_error_response("Bad request.", 400, "Bad input type.")

    logger.info("REQUEST: %s", event)

    response = update_handler.process_update(event)
    logger.info("RESPONSE: %s", response)
    return response


def send_message_to_conference_group(event, context):
    pass
