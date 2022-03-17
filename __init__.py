from mycroft import MycroftSkill, intent_file_handler


class Deutlicher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('deutlicher.intent')
    def handle_deutlicher(self, message):
        self.speak_dialog('deutlicher')


def create_skill():
    return Deutlicher()

