from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os
from kivy.app import App

kv_path = os.path.join(os.path.dirname(__file__), 'start_screen.kv')
Builder.load_file(kv_path)

class StartScreen(Screen):
     player_name = ''
     def on_start_button(self):
        player_name = self.ids.name_input.text.strip()
        if player_name:
            App.get_running_app().player_name = player_name
            self.manager.current = 'level_1'