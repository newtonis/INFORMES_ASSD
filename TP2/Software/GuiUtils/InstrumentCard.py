import tkinter as tk
from Globals import config


class InstrumentCard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.setView(self)

        self.configure(background="#bfbdb9")

        self.leftFrame = tk.Frame(self)
        self.rightFrame = tk.Frame(self)

        self.textTitle = tk.Label(
            self.leftFrame,
            height=1,
            width=25,
            text=self.controller.getInstrumentName(),
            font=config.LARGE_FONT,
            background="#bfbdb9"
        )

        self.textTitle.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1
        )

        self.buttonPlay = tk.Button(
            self.rightFrame,
            height=1,
            width=20,
            text="Escuchar",
            background="light goldenrod",
            font=config.SMALLEST_FONT,
            command=self.configure
        )

        self.buttonSelect = tk.Button(
            self.rightFrame,
            height=1,
            width=20,
            text="Seleccionar",
            background="#0ecc4e",
            font=config.SMALLEST_FONT,
            command=self.controller.getOnSelectedListener().onAction
        )

        self.buttonPlay.grid(
            column=0,
            row=0
        )

        self.buttonSelect.grid(
            column=0,
            row=1
        )

        self.leftFrame.grid(column=0, row=0)
        self.rightFrame.grid(column=1, row=0)

        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1)

    def enable(self):
        self.configure(
            background="#519457"
        )
        self.textTitle.configure(
            background="#519457"
        )

    def disable(self):
        self.configure(
            background="#bfbdb9"
        )
        self.textTitle.configure(
            background="#bfbdb9"
        )
