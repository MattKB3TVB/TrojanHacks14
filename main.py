from kivy.app import App
import kivy.properties
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.widget import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random
import webcolors

class ButtonGame():
    #Initial Conditions
    color_array = ["red", "orange", "yellow", "green", "blue", "purple"]
    colorTrue = 0
    wins = 0
    word_color = ["", ""]
    random.seed()

    #Each round
    def setTask():
        colorTrue = random.randint(0,1)
        word_color[0] = color_array[random.randint(0,5)]
        word_color[1] = color_array[random.randint(0,5)]
    
        button1 = Button(text= color_array[0], font_size=14)
        button1.bind(on_press = checkButtons(0))
        with button1.canvas:
            color_triplet = name_to_rgb_percent(color_array[0])
            Color(color_triplet[0], color_triplet[1], color_triplet[2])
            Rectangle(pos = (10,10), size= (50,50))
        button2 = Button(text= color_array[1], font_size=14)
        button3 = Button(text= color_array[2], font_size=14)
        button4 = Button(text= color_array[3], font_size=14)
        button5 = Button(text= color_array[4], font_size=14)
        button6 = Button(text= color_array[5], font_size=14)

    def checkButtons(button_press):
        if word_color[colorTrue]== color_array[button_press]:
            checkScore(True)
        else:
            checkScore(False)

    def checkScore(success):
        if success:
            wins++
            setTask()
        else:
            Lose()

    def Lose():
        self.canvas.clear()
        score_message = "You lost \n Total Score: %d \n Play again?" % wins
        end_message = Label(text = score_message, font_size=20)
        yes_button = Button(text = "Yes", font_size=14)
        yes_button.bind(onpress = Restart())
        with yes_button.canvas:
            Color(0.0, 1.0,0.0)
            Rectangle(pos = (10,10), size=(50,50))
        no_button = Button(text = "No", font_size = 14)
        with no_button.canvas:
            Color(0.0, 1.0, 0.0)
            Rectangle((70, 10), size = (50,50))

    def Restart():
        wins = 0
        setTask()

class ButtonApp(App):
    def build(self):
        game = ButtonGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    ButtonApp().run()
