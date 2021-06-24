from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class Project(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, Project",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


Project().run()