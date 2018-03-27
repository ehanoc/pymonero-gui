import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.config import Config
from kivy.logger import Logger
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 400)

#Config.set('graphics', 'resizable', 'False')
#Config.set('graphics', 'borderless', 'True')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.properties import StringProperty

Builder.load_file('circle.kv')

class RootWidget(GridLayout):
    main_label = StringProperty()

    def on_touch_down(self, touch):
        # return the result (depending what you want.)
        Logger.info('Application: touched down!')
        self.main_label = str(" testing ")
        return True

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()
