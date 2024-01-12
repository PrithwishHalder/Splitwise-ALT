# KivyMD modules
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

# Kivy modules
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.logger import Logger

# Screen
from components.appLoader.appLoader import AppLoader
from components.login.login import Login
from components.signup.signup import Signup
from components.home.home import Home
from components.account.account import Account
from components.analysis.analysis import Analysis
from components.profile.profile import Profile


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Local data
        self.saved_data = JsonStore("data.json")

    #     self.current_screen = "signup"

    def load_first_screen(self, dt):
        try:
            if self.saved_data.exists("user"):
                Logger.info(self.saved_data.get("user"))
                self.current = "home"
            else:
                Logger.info("No User available")
                self.current = "login"

        except KeyError:
            Logger.info("No User available")
            self.current = "login"

    def on_start(self):
        Clock.schedule_once(self.load_first_screen, 2)

    def navigate(self, screen):
        self.manager.current = screen
        bottom_navigation = self.manager.root.ids.bottom_navigation
        print(bottom_navigation)
        # tab_index = self.root.manager.screen_names.index(screen_name)  # Get tab index
        # bottom_navigation.current_tab = tab_index


class EvenlySpacedMDBoxLayout(MDBoxLayout):
    spacing = NumericProperty(dp(50))  # Adjust spacing as needed

    def on_size(self, *args):
        num_children = len(self.children)
        if num_children > 1:
            child_width = (self.width - self.spacing * (num_children - 1)) / num_children
            for child in self.children:
                child.size_hint_x = None
                child.width = child_width


class SplitwiseALTApp(MDApp):
    """
    SplitwiseALT Application class
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.screen_manager = MyScreenManager()
        # Screen Width and Height
        self.screen_width = Window.width
        self.screen_height = Window.height

    @staticmethod
    def validate_input(instance, text, field_type):
        """

        :param instance:
        :param text:
        :param field_type:
        """
        instance.helper_text_mode = "persistent"
        print(field_type, text)
        if text == "":
            instance.helper_text = "Required"
        else:
            instance.helper_text = ""
        pw_check = "Need to contain 8 length with"
        if field_type == "password" and not text.isdigit():
            pw_check += " 1 digit"
        if field_type == "password" and not text.isdigit():
            pw_check += " 1 digit"

        if field_type == "cnf_password":
            pass

    def change_theme(self):
        # theme_icon = self.root.ids.theme_icon
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            # theme_icon.icon = "weather-sunny"  # Change the icon to represent light theme
        else:
            self.theme_cls.theme_style = "Dark"
            # theme_icon.icon = "weather-night"

    def navigate(self, screen):
        self.screen_manager.navigate(screen)

    def build(self):
        # screen = Screen()

        # for resizing window
        # self.bind(on_start=self.adjust_padding)

        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file("app.kv")
        self.screen_manager.on_start()
        self.screen_manager.add_widget(AppLoader(name="apploader"))
        self.screen_manager.add_widget(Login(name="login"))
        self.screen_manager.add_widget(Signup(name="signup"))
        self.screen_manager.add_widget(Home(name="home"))
        self.screen_manager.add_widget(Account(name="account"))
        self.screen_manager.add_widget(Analysis(name="analysis"))
        self.screen_manager.add_widget(Profile(name="profile"))
        return self.screen_manager
