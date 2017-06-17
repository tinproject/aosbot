from functools import partial

import pytest


# TODO: generate_error_response tests


@pytest.fixture()
def bot():
    from aosbot import telegram_webhook_handler
    return partial(telegram_webhook_handler, context={})


@pytest.mark.parametrize("input_msg", [list((1,)), "string", 2, 3.14, None])
def test_webhook_error_for_non_dict_lambda_input_type(bot, input_msg):
    response = bot(input_msg)
    assert "error" in response.keys(), "Should get an error response with non mapping input types"
