from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty


class PasswordTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()