import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from tg.update_handler import UpdateHandler


config = {
    "bot_api_token": os.getenv("BOT_API_TOKEN", "FAKE:TOKEN"),
    "bot_username": os.getenv("BOT_USERNAME", "AOSBot"),
    "webhook_url": os.getenv("WEBHOOK_URL", "https://your.bot/webhook/path"),
}


def generate_error_response(error, error_code=400, error_message=""):
    error_message = {
        "error": error,
        "error_code": error_code,
        "error_message": error_message,
    }
    return error_message


def not_implemented_handler(message):
    return generate_error_response("NOT IMPLEMENTED", 500)


update_handler = UpdateHandler(
    message=not_implemented_handler,
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
