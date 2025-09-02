import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# Carica le schermate base
from .home_screen import HomeScreen
from .game_screen import GameScreen
from .story_screen import StoryScreen
from .start_screen import StartScreen
from .timeup_popup import TimeUpPopup


# Importa i livelli 
from levels.level_1 import Level1Screen
from levels.level_2 import Level2Screen
from levels.level_3 import Level3Screen

from functions.save_load import SaveLoadManager

# Percorso della cartella corrente
KV_DIR = os.path.dirname(__file__)

# Carica i file .kv delle schermate base
Builder.load_file(os.path.join(KV_DIR, "home_screen.kv"))
Builder.load_file(os.path.join(KV_DIR, "game_screen.kv"))
Builder.load_file(os.path.join(KV_DIR, "story_screen.kv"))
Builder.load_file(os.path.join(KV_DIR, "start_screen.kv"))


# Carica i file .kv dei livelli
Builder.load_file("levels/level_1.kv")
Builder.load_file("levels/level_2.kv")
Builder.load_file("levels/level_3.kv")


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Aggiungi schermate principali
        self.add_widget(HomeScreen(name="home"))
        self.add_widget(GameScreen(name="game"))
        self.add_widget(StoryScreen(name="story"))
        self.add_widget(StartScreen(name="start"))
        

        # Aggiungi schermate dei livelli
        self.add_widget(Level1Screen(name="level1"))
        self.add_widget(Level2Screen(name="level2"))
        self.add_widget(Level3Screen(name="level3"))

        self.save_load = SaveLoadManager()