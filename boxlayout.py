from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

Builder.load_file("boxlayout.kv")
Builder.load_file("gridlayout.kv")
class CalcBox(BoxLayout):
    def __int__(self, **kwargs):
        super(CalcBox, self).__int__(**kwargs)
