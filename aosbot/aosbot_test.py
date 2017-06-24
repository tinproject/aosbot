from functools import partial

import pytest

# Magic strings
NOT_IMPLEMENTED = "NOT IMPLEMENTED"


# TODO: generate_error_response tests


@pytest.fixture()
def bot():
    from aosbot import telegram_webhook_handler
    return partial(telegram_webhook_handler, context={})


@pytest.mark.parametrize("input_msg", [list((1,)), "string", 2, 3.14, None])
def test_webhook_error_for_non_dict_lambda_input_type(bot, input_msg):
    response = bot(input_msg)
    assert "error" in response, "Should get an error response with non mapping input types"


@pytest.fixture()
def update():
    def get_update_payload(payload_type, payload):
        update_event = {"update_id": 10, payload_type: payload}
        return update_event
    return get_update_payload


class TestMessageUpdates:
    FROM_USER = {"id": 42, "first_name": "A", "username": "tinproject", "language_code": "es"}
    PRIVATE_CHAT = {"id": 42, "first_name": "A", "username": "tinproject", "type": "private"}

    @pytest.fixture()
    def text_message(self, update):
        def get_message_payload(text, from_user=self.FROM_USER, chat=self.PRIVATE_CHAT):
            message = {"message_id": 1,
                       "from": from_user,
                       "chat": chat,
                       "date": 1497790000,
                       "text": text,
                       }
            return update("message", message)
        return get_message_payload

    def test_message_update_implemented(self, bot, text_message):
        message = text_message("Hola")
        response = bot(message)
        assert "error" not in response or response["error"] != "NOT IMPLEMENTED"

    @pytest.fixture()
    def text_message_response_from_private_chat(self, bot, text_message):
        def get_text_message_response_from_private_chat(text):
            message = text_message(text, self.FROM_USER, self.PRIVATE_CHAT)
            response = bot(message)
            assert response["method"] == "sendMessage", "The response must be a sendMessage method."
            return response["text"]
        return get_text_message_response_from_private_chat

    def test_start_command(self, text_message_response_from_private_chat):
        text_response = text_message_response_from_private_chat("/start")
        assert "Hola" in text_response

    def test_help_command(self, text_message_response_from_private_chat):
        text_response = text_message_response_from_private_chat("/help")
        assert "ayuda" in text_response

    def test_ahora_command(self, text_message_response_from_private_chat):
        text_response = text_message_response_from_private_chat("/ahora")
        assert text_response != ""

    def test_siguientes_command(self, text_message_response_from_private_chat):
        text_response = text_message_response_from_private_chat("/siguientes")
        assert text_response != ""

    def test_programa_command(self, text_message_response_from_private_chat):
        text_response = text_message_response_from_private_chat("/agenda")
        assert len(text_response) > 10
        assert len(text_response) < 5500

    def test_talks_load(self):
        from .talks import talks_data
        assert talks_data
        assert len(talks_data) > 0


class TestEditedMessageUpdates:
    @pytest.fixture()
    def edited_message(self, update):
        payload = {}
        return update("edited_message", payload)

    def test_edited_message_update_not_implemented(self, bot, edited_message):
        assert bot(edited_message)["error"] == NOT_IMPLEMENTED


class TestChannelPostUpdates:
    @pytest.fixture()
    def channel_post(self, update):
        payload = {}
        return update("channel_post", payload)

    def test_channel_post_update_not_implemented(self, bot, channel_post):
        assert bot(channel_post)["error"] == NOT_IMPLEMENTED


class TestEditedChannelPostUpdates:
    @pytest.fixture()
    def edited_channel_post(self, update):
        payload = {}
        return update("edited_channel_post", payload)

    def test_edited_channel_post_update_not_implemented(self, bot, edited_channel_post):
        assert bot(edited_channel_post)["error"] == NOT_IMPLEMENTED


class TestInlineQueryUpdates:
    @pytest.fixture()
    def inline_query(self, update):
        payload = {}
        return update("inline_query", payload)

    def test_inline_query_update_not_implemented(self, bot, inline_query):
        assert bot(inline_query)["error"] == NOT_IMPLEMENTED


class TestChosenInlineResultUpdates:
    @pytest.fixture()
    def chosen_inline_result(self, update):
        payload = {}
        return update("chosen_inline_result", payload)

    def test_chosen_inline_result_update_not_implemented(self, bot, chosen_inline_result):
        assert bot(chosen_inline_result)


class TestCallbackQueryUpdates:
    @pytest.fixture()
    def callback_query(self, update):
        payload = {}
        return update("callback_query", payload)

    def test_callback_query_update_not_implemented(self, bot, callback_query):
        assert bot(callback_query)["error"] == NOT_IMPLEMENTED


class TestShippingQueryUpdates:
    @pytest.fixture()
    def shipping_query(self, update):
        payload = {}
        return update("shipping_query", payload)

    def test_shipping_query_update_not_implemented(self, bot, shipping_query):
        assert bot(shipping_query)["error"] == NOT_IMPLEMENTED


class TestPreCheckoutQueryUpdates:
    @pytest.fixture()
    def pre_checkout_query(self, update):
        payload = {}
        return update("pre_checkout_query", payload)

    def test_pre_checkout_query_update_not_implemented(self, bot, pre_checkout_query):
        assert bot(pre_checkout_query)["error"] == NOT_IMPLEMENTED
