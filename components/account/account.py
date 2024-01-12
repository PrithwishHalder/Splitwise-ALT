from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from time import sleep
from config.constants import LOCAL_DATA


class Account(Screen):

    def on_enter(self):
        try:
            print(self.manager.ids)
            print(type(self.ids.navigation))
            print(self.ids.navigation)
            print(self.ids.navigation.__obj__)
        except Exception as e:
            print(e)
