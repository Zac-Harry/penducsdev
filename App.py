import tkinter as tk

class App():
    def __init__(self):
        self.init_widgets()

    def initGame(self):
        pass

    def init_widgets(self):
        self.tk = tk.Tk()
        self.tk.geometry("1000x500")
        IMG_Image = tk.PhotoImage(file = "img/bonhomme1.gif")
        self.canvas = tk.Canvas(self.tk, bg = "white" , width = 500, height = 500)
        self.canvas.create_image(50,10, image = IMG_Image ,  anchor = "nw")
        self.canvas.pack(side = "right")
        # self.canvas.pack()
        self.word = tk.Label(self.tk, text="M__")
        self.word.pack()
        self.feedback = tk.Label(self.tk, text="Proposez une lettre")
        self.feedback.pack()
        self.submit = tk.Button(self.tk, text="Proposer", command=self.submit_char)
        self.submit.pack()

    def submit_char(self):
        pass

if __name__ == "__main__":
    app = App()
    app.tk.title("Pendu ;(")
    app.tk.mainloop()
