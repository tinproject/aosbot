import pytest

from .update_handler import UpdateHandler, UPDATE_TYPES


@pytest.mark.parametrize("update_type", UPDATE_TYPES)
def test_update_handler_creation_with_one_valid_handler(update_type):
    updates = {k: v for k, v in [(update_type, lambda x: x)]}
    uh = UpdateHandler(**updates)
    assert update_type in uh.type_handlers


def test_update_handler_creation_with_more_tha_one_valid_handlers():
    update_types = [UPDATE_TYPES[i] for i in range(4)]
    updates = {k: lambda x: x for k in update_types}
    uh = UpdateHandler(**updates)
    for update_type in update_types:
        assert update_type in uh.type_handlers


@pytest.mark.parametrize("update_type", ["invalid_payload"])
def test_update_handler_creation_fail_with_only_invalid_types_handler(update_type):
    updates = {k: v for k, v in [(update_type, lambda x: x)]}
    with pytest.raises(ValueError):
        UpdateHandler(**updates)
