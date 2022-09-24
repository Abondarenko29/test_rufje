from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from text import *



#Констанкти
H = "horizontal"
V = "vertical"
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"



class Init_screen (Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        label= Label (text = init_txt)
        imja_label = Label(text = "Введіть ваше ім'я")
        wik_label = Label(text = "Введіть ваш вік")
        self.imja = TextInput (multiline = False)
        self.wik = TextInput (multiline = False)
        daliB = uixB (self, goal = "1", direction = LEFT, on_press_ = self.zminni, text = "Далі")

        MainLine = BoxLayout (orientation = V)
        nameLayout = BoxLayout (orientation = H, size_hint = (1, .2))
        yearsoldLayout = BoxLayout (orientation = H, size_hint = (1, .2))

        nameLayout.add_widget (imja_label)
        nameLayout.add_widget (self.imja)

        yearsoldLayout.add_widget (wik_label)
        yearsoldLayout.add_widget (self.wik)

        MainLine.add_widget(label)

        MainLine.add_widget (nameLayout)
        MainLine.add_widget (yearsoldLayout)

        MainLine.add_widget (daliB)

        self.add_widget(MainLine)

    def zminni (self):

        global wik
        wik = self.wik.text

        global imja
        imja = self.imja.text

class First_test_screen (Screen):
    def __init__ (self, **kwargs):
        super ().__init__ (**kwargs)

        MainLine = BoxLayout (orientation = V)
        puvlvs_layout = BoxLayout (orientation = H)
        buttonLine = BoxLayout (orientation = V)

        self.puvlvs = TextInput ()

        daliB = uixB (self, 
            goal = "2",
            direction = LEFT,
            text = "Далі",
            on_press_ = self.zminni
        )

        label = Label (text = txt_test1)

        puvlvs_layout.add_widget (Label (text = "Введіть результат:"))
        puvlvs_layout.add_widget (self.puvlvs)

        buttonLine.add_widget (daliB)

        MainLine.add_widget (label)
        MainLine.add_widget (puvlvs_layout)
        MainLine.add_widget (buttonLine)

        self.add_widget (MainLine)

    def zminni (self):

        global puvlvs
        puvlvs = self.puvlvs.text

class Second_test_screen (Screen):
    def __init__ (self, **kwargs):
        super ().__init__ (**kwargs)
        MainLine = BoxLayout (orientation = V)

        label = Label (text = txt_test2)

        next_b = uixB (self,
            goal = "3",
            direction = LEFT,
            text = "Почати"
        )

        MainLine.add_widget (label)
        MainLine.add_widget (next_b)

        self.add_widget (MainLine)

class Third_test_screen (Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        label = Label (text = txt_test2)
        second_rezuvlvtat_label = Label(text = "Результат:")
        cej_rezuvlvtat_label = Label(text = "Результат після відпочинку:")
        self.second_rezuvlvtat = TextInput (multiline = False)
        self.cej_rezuvlvtat = TextInput (multiline = False)
        endB = uixB (self, goal = "deinit", direction = LEFT, on_press_ = self.zminni, text = "Завершити")

        MainLine = BoxLayout (orientation = V)
        second_rezuvlvtat_layout = BoxLayout (orientation = H)
        cej_rezuvlvtat_layout = BoxLayout (orientation = H)

        second_rezuvlvtat_layout.add_widget (second_rezuvlvtat_label)
        second_rezuvlvtat_layout.add_widget (self.second_rezuvlvtat)

        cej_rezuvlvtat_layout.add_widget (cej_rezuvlvtat_label)
        cej_rezuvlvtat_layout.add_widget (self.cej_rezuvlvtat)

        MainLine.add_widget(label)

        MainLine.add_widget (second_rezuvlvtat_layout)
        MainLine.add_widget (cej_rezuvlvtat_layout)

        MainLine.add_widget (endB)

        self.add_widget(MainLine)

    def zminni (self):

        global second_rezuvlvtat
        second_rezuvlvtat = self.second_rezuvlvtat.text

        global cej_rezuvlvtat
        cej_rezuvlvtat = self.cej_rezuvlvtat.text

class Deinit_screen (Screen):
    def __init__ (self, name, **kwargs):
        super ().__init__ ()
        self.name = name

        MainLine = BoxLayout (orientation = V)
        label = Label (text = deinit_txt)

        MainLine.add_widget (label)

        self.add_widget (MainLine)







class RufjeApp (App):
    def build (self):
        sm = ScreenManager ()

        sm.add_widget (Init_screen(name = "init"))
        sm.add_widget (First_test_screen(name = "1"))
        sm.add_widget (Second_test_screen(name = "2"))
        sm.add_widget (Third_test_screen(name = "3"))
        sm.add_widget (Deinit_screen(name = "deinit"))

        return sm




class uixB (Button):
    def __init__ (self, screen, goal, direction, on_press_ = None, **kwargs):
        super ().__init__ (**kwargs)
        self.screen = screen
        self.goal = goal
        self.direction = direction
        self.on_press_ = on_press_

    def on_press (self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
        if self.on_press_ != None:
            self.on_press_ ()

rufje = RufjeApp ()
rufje.run ()

print (f"(\"{imja}\" \"{wik}\" \"{puvlvs}\" \"{second_rezuvlvtat}\" \"{cej_rezuvlvtat}\")")