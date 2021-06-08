from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window


class PongPaddle(Widget):
    pass


class PongBall(Widget):
    pass


class PongGame(Widget):
    pass


class MainApp(App):
    def build(self):
        game = PongGame()
        return game


MainApp().run()
