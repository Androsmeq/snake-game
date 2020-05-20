from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from  kivy.uix.anchorlayout import AnchorLayout

class main_page(AnchorLayout, GridLayout):
    def quit(self, a):
        quit()
    def miss(self, a):
        self.ballx=2
        self.bally=2
        Clock.schedule_once(self.aparitie, 0)
        self.jos = 0
        self.stanga = 0
        self.sus = 0
        self.dreapta = 0



    def __init__(self, **kwargs):

        self.spacing=10

        self.line = 0
        self.ballx= 2
        self.bally= 2
        self.bbb = 60
        self.aaa=20
        super(main_page, self).__init__(**kwargs)
        #self.orientation="vertical"
        #self.font_name= "Arial"
        self.add_widget(Label(text="Welcome to Snake", font_size=45))
        self.stanga = 0
        self.sus = 0
        self.jos = 0
        self.dreapta = 0
        Clock.schedule_once(self.my_callback, 1)
    def s(self, a):
        self.stanga = 1
        self.sus = 0
        self.jos = 0
        self.dreapta = 0

    def su(self, a):
        self.sus = 1
        self.stanga = 0
        self.jos = 0
        self.dreapta = 0
    def jo(self, a):
        self.jos = 1
        self.stanga = 0
        self.sus = 0
        self.dreapta = 0
    def dr(self, a):
        self.dreapta = 1
        self.stanga = 0
        self.sus = 0
        self.jos = 0

    def my_callback(self, dt):
        self.clear_widgets()
        Clock.schedule_interval(self.aparitie, .1)

    def aparitie(self, dt):
            sus = AnchorLayout(anchor_x='center', anchor_y='top')
            sstanga= AnchorLayout(anchor_x='left', anchor_y='bottom')
            ccentru = AnchorLayout(anchor_x='center', anchor_y='bottom')
            ddreapta = AnchorLayout(anchor_x='right', anchor_y='bottom')
            xsusxxxa=AnchorLayout(anchor_x='left', anchor_y='top')
            rretry = AnchorLayout(anchor_x='right', anchor_y='bottom')
            layout = GridLayout(cols=1, size_hint=(0.25,0.2))
            self.clear_widgets()
            root = StackLayout()
            self.line=0
            self.text = "\n"*(int(self.aaa))
            if self.ballx==0 or self.ballx==self.aaa+1 or self.bally<=0 or self.bally >=self.bbb+1:
                ccentru.clear_widgets()
                sus.clear_widgets()
                sstanga.clear_widgets()
                ddreapta.clear_widgets()
                self.clear_widgets()
                mort = Label(text="Game over!")
                self.add_widget(mort)
                retry=Button(text="Retry", font_size=30, size_hint=(1, .2))
                retry.bind(on_press=self.miss)

                rretry.add_widget(retry)
                self.add_widget(rretry)
                return


            for x in range(self.aaa):
                ssss = AnchorLayout(anchor_x='center', anchor_y='top')
                n1=Label(text="Smeq Sneak", size=(100, 100), size_hint=(None, None), font_size=50)
                ssss.add_widget(n1)
                self.add_widget(ssss)

                self.line+=1
                if self.line==self.ballx:
                    self.text+="\n"+"."*(self.bally-1)+unichr(2764)+"."*(self.bbb-self.bally-1)
                else:
                    self.text+="\n"+"."*self.bbb
            sus.add_widget(Label(text=self.text, size_hint=(.25, .2)))
            self.add_widget(sus)

            stanga = Button(text='<', font_size=34,size_hint=(.375,0.2))
            sstanga.add_widget(stanga)
            self.add_widget(sstanga)
            stanga.bind(on_press=self.s)

            sus = Button(text="^", font_size=39, size_hint=(100, 1))
            layout.add_widget(sus)

            sus.bind(on_press=self.su)
            jos = Button(text='v', font_size=31,size_hint=(100, 1))
            layout.add_widget(jos)
            ccentru.add_widget(layout)
            self.add_widget(ccentru)
            jos.bind(on_press=self.jo)
            dreapta = Button(text='>', font_size=34, size_hint=(.375, .2))
            ddreapta.add_widget(dreapta)
            self.add_widget(ddreapta)
            dreapta.bind(on_press=self.dr)

            if self.stanga==1:
                self.bally -=3
            if self.sus==1:
                self.ballx-=1
            if self.jos==1:
                self.ballx+=1
            if self.dreapta==1:
                self.bally+=3



class MyApp(App):

    def build(self):
        return main_page()


if __name__ == '__main__':
    MyApp().run()