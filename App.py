import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.init_widgets()

    def initGame(self):
        pass

    def init_widgets(self):
        self.canvas = tk.Canvas(self, bg="white", height=500, width=1000)
        self.canvas.pack()
        self.word = tk.Label(self, text="M__")
        self.word.pack()
        self.feedback = tk.Label(self, text="Proposez une lettre")
        self.feedback.pack()
        self.submit = tk.Button(self, text="Proposer", command=self.submit_char)
        self.submit.pack()

    def submit_char(self):
        pass
