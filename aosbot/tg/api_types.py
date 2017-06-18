import datetime as dt


class TGAPIBase:
    mandatory_keys = {
        # key_name: callable_to_convert_value
    }
    optional_keys = {
        # key_name: (callable_to_convert_value, default_value)
    }

    def __init__(self, input_dict):
        for k, v in self.mandatory_keys.items():
            if k in input_dict and not isinstance(v, str):
                setattr(self, k, v(input_dict.get(k)))
            elif isinstance(v, str):
                # The callable to convert the value is an string
                # This is needed for self referencing classes
                # Do nothing here, MUST set on the subclass
                pass
            else:
                raise TypeError(f"Key {k} is mandatory")
        for k, v in self.optional_keys.items():
            if k in input_dict:
                if isinstance(v[0], str):
                    # Same as above
                    # Do nothing here, MUST set on the subclass
                    pass
                else:
                    setattr(self, k, v[0](input_dict.get(k)))
            else:
                setattr(self, k, v[1])

    def to_dict(self):
        return dict(self)

    def __iter__(self):
        for k in self.mandatory_keys:
            v = getattr(self, k)
            if hasattr(v, "to_dict"):
                yield (k, v.to_dict())
            else:
                yield (k, v)
        for k in self.optional_keys:
            v = getattr(self, k)
            if v is not None:
                if hasattr(v, "to_dict"):
                    yield (k, v.to_dict())
                else:
                    yield (k, v)

    def __str__(self):
        text = "{"
        for k in self.mandatory_keys:
            v = getattr(self, k)
            text += f"{k}: {v}, "
        for k in self.optional_keys:
            v = getattr(self, k)
            text += f"{k}: {v}, "
        text += "}"
        return text


class User(TGAPIBase):
    mandatory_keys = {
        "id": int,
        "first_name": str,
    }
    optional_keys = {
        "last_name": (str, ""),
        "username": (str, ""),
        "language_code": (str, None),
    }

    def __str__(self):
        return f"User: {self.first_name} { self.last_name} (id: {self.id} / {self.username})"


class UserList(list):
    pass


class Chat(TGAPIBase):
    mandatory_keys = {
        "id": int,
        "type": str,
    }
    optional_keys = {
        "title": (str, ""),
        "username": (str, ""),
        "first_name": (str, ""),
        "last_name": (str, ""),
        "all_members_are_administrators": (bool, None),
         }


class MessageEntity(dict):
    # Not implemented
    pass


class MessageEntityList(list):
    pass


class Audio(dict):
    # Not implemented
    pass


class Document(dict):
    # Not implemented
    pass


class Game(dict):
    # Not implemented
    pass


class Sticker(dict):
    # Not implemented
    pass


class Video(dict):
    # Not implemented
    pass


class Voice(dict):
    # Not implemented
    pass


class VideoNote(dict):
    # Not implemented
    pass


class Contact(dict):
    # Not implemented
    pass


class Location(dict):
    # Not implemented
    pass


class Venue(dict):
    # Not implemented
    pass


class PhotoSize(dict):
    # Not implemented
    pass


class PhotoSizeList(list):
    pass


class Invoice(dict):
    # Not implemented
    pass


class SuccessfullPayment(dict):
    # Not implemented
    pass


class Message(TGAPIBase):
    mandatory_keys = {
        "message_id": int,
        "date": dt.datetime.fromtimestamp,
        "chat": Chat,
    }
    optional_keys = {
        "from": (User, None),
        "forward_from": (User, None),
        "forward_from_chat": (Chat, None),
        "forward_from_message_id": (int, None),
        "forward_date": (dt.datetime.fromtimestamp, None),
        "reply_to_message": ("Message", None),
        "edit_date": (dt.datetime.fromtimestamp, None),
        "text": (str, None),
        "entities": (MessageEntityList, None),
        "audio": (Audio, None),
        "document": (Document, None),
        "game": (Game, None),
        "photo": (PhotoSizeList, None),
        "sticker": (Sticker, None),
        "video": (Video, None),
        "voice": (Voice, None),
        "video_note": (VideoNote, None),
        "new_chat_members": (UserList, None),
        "caption": (str, None),
        "contact": (Contact, None),
        "location": (Location, None),
        "venue": (Venue, None),
        "new_chat_member": (User, None),
        "left_chat_member": (User, None),
        "new_chat_title": (str, None),
        "new_chat_photo": (PhotoSizeList, None),
        "delete_chat_photo": (bool, None),
        "group_chat_created": (bool, None),
        "supergroup_chat_created": (bool, None),
        "channel_chat_created": (bool, None),
        "migrate_to_chat_id": (int, None),
        "migrate_from_chat_id": (int, None),
        "pinned_message": ("Message", None),
        "invoice": (Invoice, None),
        "successful_payment": (SuccessfullPayment, None),
    }

    def __init__(self, input_dict):
        super().__init__(input_dict)

        # set nested Message types
        for k in ("reply_to_message", "reply_to_message", "pinned_message"):
            if k in input_dict:
                setattr(self, k, Message(input_dict[k]))
            else:
                setattr(self, k, self.optional_keys[k][1])
