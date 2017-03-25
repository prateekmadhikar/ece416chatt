import json


def serialize(obj):
    return json.dumps(obj).encode('utf-8')


class User:

    def __init__(self, name, id, socket):
        self.name = name
        self.id = id
        self.socket = socket

    def __eq__(self, other):
        return self.id == other.id

    @property
    def is_alive(self):
        message = {
            'type': 'status'
        }

        try:
            self.socket.send(serialize(message))
            return True
        except Exception:
            return False

    def send_message(self, group, from_user, message):
        message = {
            'group': group.id,
            'from': from_user.id,
            'message': message
        }

        self.socket.send(serialize(message))