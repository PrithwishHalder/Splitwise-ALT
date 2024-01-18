from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
from config.constants import LOCAL_DATA


class Home(Screen):

    label_data = StringProperty()

    def on_enter(self):
        self.label_data = str(LOCAL_DATA.get("user"))
        # for id, instance in self.ids.items():
        #     print(id, instance)
        #     if id == 'home':
        #         print(id)
        #         instance.text_color = 0,0,1,1



