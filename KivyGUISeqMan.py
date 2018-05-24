#kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.dropdown import DropDown
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Entry = ""
Query = ""
ReverseQuery = ""

ReverseComp = ""


class SeqInput(TextInput):

    pass


class WindowLayout(FloatLayout):
    Entry = ""
    Query = ""
    ReverseQuery = ""
    ReverseComp = ""
    def Complement(self, Seq):
        Complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
        CompQuery = ""
        Seq = Seq.upper()
        for nt in Seq:
            try:
                CompQuery += Complement[nt]

            except:
                CompQuery += nt
        return CompQuery


class DNAManagerApp(App):
    def build(self):
        return WindowLayout()


DNAManagerApp().run()
