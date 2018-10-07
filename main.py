from kivy.app import App
from boxlayout import CalcBox
from gridlayout import GridLayout
from kivy.lang.builder import Builder



class CalcApp(App):
    def build(self):
        return CalcBox()


if __name__ == '__main__':
    CalcApp().run()