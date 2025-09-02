from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty

class GameScreen(Screen):
    current_level = NumericProperty(0)
    """Binds to <GameScreen> in game_screen.kv"""
    def on_help(self):
        # Seleziona l'immagine in base al livello
        if self.current_level == 0:
            help_image = "resources/images/levels_info.jpg"
        elif self.current_level == 1:
            help_image = "resources/images/help_info.jpg"
        elif self.current_level == 2:
            help_image = "resources/images/help_info2.jpg"
        else:
            help_image = "resources/images/levels_info3.jpg"

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Image(source=help_image))

        popup = Popup(
            title="Help",
            content=layout,
            size_hint=(0.9, 0.9),
            auto_dismiss=True
        )
        popup.open()
        
    def restart_level(self):
        # Chiama il livello giusto e lo resetta
        if self.current_level == 1:
            self.manager.get_screen("level1").reset_level()
        elif self.current_level == 2:
            self.manager.get_screen("level2").reset_level()
        elif self.current_level == 3:
            self.manager.get_screen("level3").reset_level()