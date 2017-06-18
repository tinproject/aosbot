from .api_types import TGAPIBase, User, Chat


class Leaf(TGAPIBase):
    mandatory_keys = {"id": int}
    optional_keys = {"a": (int, 4), "b": (str, "")}


class Root(TGAPIBase):
    mandatory_keys = {"root": Leaf}
    optional_keys = {"l": ("Root", None), "r": (Leaf, None)}

    def __init__(self, input_dict):
        super().__init__(input_dict)
        if "l" in input_dict:
            setattr(self, "l", Root(input_dict["l"]))


class TestTGAPIBase:
    def test_object_creation_from_dict_and_back(self):
        obj_dict = {"root": {"id": 23, "a": 3, "b": "sdf"},
                    "l": {"root": {"id": 454, "a": 3, "b": "sdf"},
                          "r": {"id": 2344, "a": 34, "b": "324"}
                          },
                    "r": {"id": 2344, "a": 34, "b": "324"}}
        r = Root(obj_dict)
        assert r
        assert r.root.id == 23

        d = dict(r)
        assert d["root"]["id"] == 23
        assert obj_dict == d


def test_user():
    user_dict = {"id": 4545, "first_name": "Pepito", "last_name": "Pérez", "username": "pepe"}
    user = User(user_dict)
    assert user.id == 4545
    assert user.username == "pepe"
    assert "pepe" in str(user)


def test_chat():
    chat_dict = {"id": 4545, "type": "private", "first_name": "Pepito",
                 "last_name": "Pérez", "username": "pepe"}
    chat = Chat(chat_dict)
    assert chat.id == 4545
    assert chat.title == ""
