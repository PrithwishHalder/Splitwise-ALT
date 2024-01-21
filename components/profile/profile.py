from kivy.uix.screenmanager import Screen
from kivy.properties import DictProperty
from config.constants import LOCAL_DATA


class Profile(Screen):

    user_data = DictProperty()

    def on_enter(self):
        self.user_data = LOCAL_DATA.get("user")
        self.ids.name.text = f"{self.user_data.get('first')} {self.user_data.get('last')}"

    def logout(self):
        LOCAL_DATA.store_clear()
        self.manager.current = "login"
