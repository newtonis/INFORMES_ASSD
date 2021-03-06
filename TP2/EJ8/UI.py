import tkinter as tk
from tkinter import *
from Menus.StartMenu import StartMenu
from Menus.PersonalizadoMenu import PersonalizadoMenu
from Menus.ReverbMenu import ReverbMenu
from Menus.ParametersConfigMenu import ParametersConfigMenu
from Menus.RealtimeOrFilenameMenu import RealtimeOrFilenameMenu
from Menus.RealtimeMenu import RealtimeMenu
from Menus.FilenameMenu import FilenameMenu
from Menus.PredefinidoMenu import PredefinidoMenu

from EffectsInterface import getEffectsInterface
from Globals import styles, config

frames = [
    StartMenu,
    PersonalizadoMenu,
    ReverbMenu,
    ParametersConfigMenu,
    RealtimeOrFilenameMenu,
    RealtimeMenu,
    FilenameMenu,
    PredefinidoMenu
]

startFrame = 0


class UI(tk.Tk):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        #self.maxsize(width=666, height=666)

        self.protocol('WM_DELETE_WINDOW', self.exitFunction)
        self.title("Generador de efectos")

        self.resizable(width=False, height=False)

        if config.debug:
            print("Comenzando aplicación principal")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for frame in frames:
            self.frames[frame] = frame(container, self)
            self.frames[frame].grid_propagate(True)
            self.frames[frame].grid(row=0, column=0, sticky=E+W+N+S)

        self.showFrame(frames[startFrame])
        self.frame = frames[startFrame]

        styles.getData().load()

        getEffectsInterface()

        #print("hello")

    def showFrame(self, frame):
        self.frames[frame].focus()
        frame = self.frames[frame]
        frame.tkraise()
        self.frame = frame

    def getCurrentFrame(self):
        return self.frame

    def run(self):
        self.mainloop()

    def exitFunction(self):
        getEffectsInterface().end()
        self.quit()
        self.destroy()


if __name__ == "__main__":
    UI().run()
