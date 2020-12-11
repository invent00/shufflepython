from kivy.config import Config
Config.set('graphics', 'width', '1440')
Config.set('graphics', 'height', '1000')

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.app import App
from kivy.clock import Clock
import random
import time 

#add japanese setting
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分

resource_add_path('c:/Windows/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'msgothic.ttc')  # 追加分


Builder.load_string('''
#:kivy 1.8.0

<KivyTimer>:
    BoxLayout:
        orientation: 'vertical'
        pos: root.pos
        size: root.size
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: str(root.name1)
                    font_size: 100
                Label:
                    text: str(root.name2)
                    font_size: 100
                Label:
                    text: str(root.name3)
                    font_size: 100
                Label:
                    text: str(root.name4)
                    font_size: 100
                Label:
                    text: str(root.name5)
                    font_size: 100
                Label:
                    text: str(root.disp6)
                    font_size: 100
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: str(root.disp1)
                    font_size: 100
                Label:
                    text: str(root.disp2)
                    font_size: 100
                Label:
                    text: str(root.disp3)
                    font_size: 100
                Label:
                    text: str(root.disp4)
                    font_size: 100
                Label:
                    text: str(root.disp5)
                    font_size: 100
                Label:
                    text: str(root.disp6)
                    font_size: 100
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1.0, 0.3

            Button:
                text: 'stop'
                font_size: 16
                on_press: root.on_command('stop')

            Button:
                text: 'Start'
                font_size: 16
                on_press: root.on_command('start/stop')

            Button:
                text: 'Reset'
                font_size: 16
                on_press: root.on_command('reset')
''')
participants=["ほげ一郎","ほげ次郎","ほげ三郎","ほげ四郎","ほげ五郎"]
presents=["ディスプレイ","イヤホン","なんか1","なんか2","なんか3"]

class KivyTimer(Widget):
    is_countdown = BooleanProperty(False)
    disp1 = StringProperty('0')
    disp2 = StringProperty('0')
    disp3 = StringProperty('0')
    disp4 = StringProperty('0')
    disp5 = StringProperty('0')
    disp6 = StringProperty('Press start!')
    name1 = StringProperty(str(participants[0]))
    name2 = StringProperty(str(participants[1]))
    name3 = StringProperty(str(participants[2]))
    name4 = StringProperty(str(participants[3]))
    name5 = StringProperty(str(participants[4]))
    def shufflepresents(self,dt):
            random.shuffle(presents)
            self.disp1 = presents[0]
            self.disp2 =presents[1]
            self.disp3= presents[2]
            self.disp4 = presents[3]
            self.disp5 = presents[4]
            self.disp6="抽選中" 
    def stoppresents(self,dt):
            Clock.unschedule(self.shufflepresents)
            self.disp6 = '抽選終了'
    def on_command(self, command):
        if command == 'stop':
            stoptime=random.randint(20,80)/100
            Clock.schedule_once(self.stoppresents,stoptime)
            

        elif command == 'start/stop':
            random.shuffle(presents)
            Clock.schedule_interval(self.shufflepresents, 0.1)   
            
        elif command == 'reset':
            self.disp1 = 'Lets start!'
        
        

    


class KivyTimerApp(App):
    def build(self):
        return KivyTimer()


if __name__ == '__main__':
    KivyTimerApp().run()