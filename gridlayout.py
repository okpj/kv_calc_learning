from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout


class CalcGrid(GridLayout):
    def __int__(self, **kwargs):
        super(CalcGrid, self).__int__(**kwargs)
