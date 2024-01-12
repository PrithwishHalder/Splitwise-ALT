from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from config.constants import LOCAL_DATA


class Profile(Screen):

    label_data = StringProperty()

    def on_enter(self):
        self.label_data = str(LOCAL_DATA.get("user"))
