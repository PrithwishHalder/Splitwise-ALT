from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.bottomnavigation import MDBottomNavigation

# Load screen KV files
Builder.load_file("screen_home.kv")
Builder.load_file("screen_profile.kv")


class MainApp(App):
    def build(self):
        # Create ScreenManager and screens
        manager = ScreenManager()
        manager.add_widget(Screen(name="home"))
        manager.add_widget(Screen(name="profile"))

        # Create MDBottomNavigation
        bottom_navigation = MDBottomNavigation()

        # Add MDBottomNavigationItems with screen names
        bottom_navigation.add_widget(MDBottomNavigationItem(name="home"))
        bottom_navigation.add_widget(MDBottomNavigationItem(name="profile"))

        # Add MDBottomNavigation to a layout
        layout = MDBoxLayout()
        layout.add_widget(bottom_navigation)
        layout.add_widget(manager)

        return layout


if __name__ == "__main__":
    MainApp().run()
