from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Reminder(MDApp):
    def build(self):
        return MDLabel(text="Hello, Reminder!", halign="center")


Reminder().run()