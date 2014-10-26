from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
import random
from webcolors import name_to_rgb_percent

class ButtonGame():
    pass

class duringGame(BoxLayout):
    def beginGame():
        #Initial Conditions
        self.canvas.clear()
        color_array = ["red", "yellow", "green", "blue"]
        colorTrue = 0
        word_color = ["", ""]
        random.seed()
        setTask()
    
    #Each round
    def setTask():
        wins = NumericProperty(0)
        colorTrue = random.randint(0,1)
        word_color[0] = color_array[random.randint(0,3)]
        word_color[1] = color_array[random.randint(0,3)]
        word_rgb_pctt = name_to_rgb_percent(word_color[1])

        #Task Label Initialize
        task_colorR = NumericProperty(word_rgb_pct[0])
        task_colorG = NumericProperty(word_rgb_pct[1])
        task_colorB = NumericProperty(word_rgb_pct[2])
        task_color = ReferenceListProperty(task_colorR, task_colorG, task_colorB)
        task_word = word_color[0]
    
        #button color initialization
        button1 = ObjectProperty(None)
        button1_colorR = NumericProperty(1.0)
        button1_colorG = NumericProperty(0)
        button1_colorB = NumericProperty(0)
        button1_color = ReferenceListProperty(button1_colorR, button1_colorG, button1_colorB)

        button2 = ObjectProperty(None)
        button2_colorR = NumericProperty(0.55)
        button2_colorG = NumericProperty(0.55)
        button2_colorB = NumericProperty(0)
        button2_color = ReferenceListProperty(button2_colorR, button2_colorG, button2_colorB)

        button3 = ObjectProperty(None)
        button3_colorR = NumericProperty(0)
        button3_colorG = NumericProperty(1.0)
        button3_colorB = NumericProperty(0)
        button3_color = ReferenceListProperty(button3_colorR, button3_colorG, button3_colorB)

        button4 = ObjectProperty(None)
        button4_colorR = NumericProperty(0)
        button4_colorG = NumericProperty(0)
        button4_colorB = NumericProperty(1.0)
        button4_color = ReferenceListProperty(button4_colorR, button4_colorG, button4_colorB)

    def checkButtons(button_press):
        if word_color[colorTrue]== color_array[button_press]:
            checkScore(True)
        else:
            checkScore(False)

    def checkScore(success):
        if success:
            self.wins += 1
            setTask()
        else:
            endGame().Lose(self.wins)

class endGame(Widget):
    def Lose(wins):
        self.canvas.clear()
        score_message = "You lost \n Total Score: %d" % wins

class ButtonApp(App):
    def build(self):
        game = ButtonGame()
        game.start()
        #Clock.schedule_interval(game.update, 1.0/60.0) Intend to set time limit later
        return game

if __name__ == '__main__':
    ButtonApp().run()

