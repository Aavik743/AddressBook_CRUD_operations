import mongoengine as me


class Users(me.Document):
    name = me.StringField(max_length=50, required=True)
    number = me.StringField(max_length=10, required=True)

    def to_dict(self):
        user_dict = {
            "Name": self.name,
            "Number": self.number
        }
        return user_dict


