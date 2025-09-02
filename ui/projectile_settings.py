from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder
from projectiles import projectile_info

# Carica il file kv relativo a questo widget
Builder.load_file("ui/projectile_settings.kv")

class ProjectileSettingsBar(BoxLayout):
    bullet_mass = NumericProperty(projectile_info.get_bullet_mass())
    bullet_radius = NumericProperty(projectile_info.get_bullet_radius())

    def on_bullet_mass(self, instance, value):
        projectile_info.set_bullet_mass(value)

    def on_bullet_radius(self, instance, value):
        projectile_info.set_bullet_radius(value)
