import logging
logger = logging.getLogger()


# Update types as Telegram BOT API 3.0
UPDATE_TYPES = [
    "message",
    "edited_message",
    "channel_post",
    "edited_channel_post",
    "inline_query",
    "chosen_inline_result",
    "callback_query",
    "shipping_query",
    "pre_checkout_query",
]


class UpdateHandler:
    def __init__(self, **kwargs):
        self.type_handlers = {}
        for k, v in kwargs.items():
            if k in UPDATE_TYPES:
                self.type_handlers[k] = v
        if not self.type_handlers:
            raise ValueError("No valid handlers for process updates")

    def process_update(self, update):
        logger.info("Processing update id: %s", update.get("update_id"))

        for update_type in UPDATE_TYPES:
            try:
                update_payload = update.get(update_type, None)
                if update_payload is not None:
                    response = self.type_handlers[update_type](update_payload)
                    return response
            except Exception as e:
                logger.error("ERROR: Can't process update type %s", update_type)
                raise e
