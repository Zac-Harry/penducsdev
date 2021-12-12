import tkinter as tk
from PIL import Image,ImageTk
import ILib

class App():
    def __init__(self):
        # sauvegarde du meilleur score
        self.bestScore = -1
        self.endGameMessage = ""
        self.init_widgets()

    def initGame(self):
        self.rdm = ILib.getRandomWord()
        self.wordNoModify = self.rdm[0]
        self.word = self.rdm[1]
        self.clear = ILib.getClearWord(self.word)
        self.end = False
        self.log = []
        self.errors = 0
        self.clear = self.unClear(self.word, self.wordNoModify, self.clear, self.word[0])
        self.log.append(self.word[0])
        self.wordLabel.configure(text = ILib.firstLetterCapital(self.clear))
        self.logLabel.configure(text=", ".join(self.log))
        # nombre maximum d'erreurs
        self.maxErrors = len(self.IMG_Image)-1

    # Fonction vérifiant si le caractère est présent.
    # retourne le nouveau mot "clean"
    def unClear(self,word, wordNoModify, clear, char):
        temp = list(clear)
        found = False
        for i in range(len(word)):
            if word[i] == char:
                temp[i] = wordNoModify[i]
                found = True
        if not found:
            print("Erreur !")
            self.errors +=1
            if(self.checkLoose()):
                self.printEndMenu("Perdu")
            else:
                self.canvas.itemconfig(self.imageCanvas,image = self.IMG_Image[self.errors])
        return ''.join(temp)

    def init_widgets(self):
        self.tk = tk.Tk()
        self.tk.geometry("1000x500")
        self.tk.configure(bg = "#2a302e")

        #Jeu
        self.packGameWidgets()
        self.gameFrame.pack_forget()
        self.tk.unbind('<Return>')
        # Menu de fin
        self.packEndGameWidgets("none")
        self.endGameFrame.pack_forget()

        # Menu
        self.packMenu()


    def packMenu(self):
        self.menuFrame = tk.Frame(self.tk)
        self.menuFrame.pack()
        self.betterScoreLabel = tk.Label(self.menuFrame, text = "Meilleur score: " + (str(self.bestScore) if self.bestScore != -1 else "Aucun"))
        self.betterScoreLabel.pack()
        self.menuPlayButton = tk.Button(self.menuFrame, text = "Jouer" , command = self.rejouer)
        self.menuPlayButton.pack()

    def packGameWidgets(self):
        self.gameFrame = tk.Frame(self.tk)
        self.gameFrame.pack()
        self.frame = tk.Frame(self.gameFrame)
        self.frame.pack(side = "left")
        # self.frame.place(relx=0.25, rely=0.25, anchor="center")
        self.IMG_Image = []
        for i in range(1,9):
            image = Image.open("img/bonhomme"+str(i)+".gif")
            image = image.resize((500, 500))
            my_img =ImageTk.PhotoImage(image)
            self.IMG_Image.append(my_img)
        self.canvas = tk.Canvas(self.gameFrame, bg = "white" , width = 500, height = 500)
        self.imageCanvas = self.canvas.create_image(0,0, image = self.IMG_Image[0] ,  anchor = "nw")
        self.canvas.pack(side = "right")

        self.betterScoreLabel = tk.Label(self.gameFrame, text = "Meilleur score: " + (str(self.bestScore) if self.bestScore != -1 else "Aucun"))
        self.betterScoreLabel.pack()
        self.wordLabel = tk.Label(self.frame, text="M....")
        self.wordLabel.grid(row=0, column=0)
        self.wordLabel.config(font=("Courier New", 44))
        self.entry = tk.Entry(self.frame)
        self.entry.grid(row=1, column=0)
        self.feedback = tk.Label(self.frame, text="Proposez une lettre!")
        self.feedback.grid(row=2, column=0)
        self.submit = tk.Button(self.frame, text="Proposer", command=self.submit_char)
        self.submit.grid(row=3, column=0)
        self.logLabel = tk.Label(self.frame, text="")
        self.logLabel.grid(row=4, column=0)
        self.tk.bind('<Return>', self.submit_char_event)

    def packEndGameWidgets(self,message):
        self.endGameFrame = tk.Frame(self.tk)
        self.endGameFrame.pack()
        self.betterScoreLabel = tk.Label(self.endGameFrame, text = "Meilleur score: " + (str(self.bestScore) if self.bestScore != -1 else "Aucun"))
        self.betterScoreLabel.pack()
        self.endGameMessageLabel = tk.Label(self.endGameFrame, text=message)
        self.endGameMessageLabel.pack()
        self.endGameRejouerButton = tk.Button(self.endGameFrame,text="Rejouer", command = self.rejouer)
        self.endGameRejouerButton.pack()
        self.endGameMenuButton = tk.Button(self.endGameFrame,text="Menu", command = self.retourMenu)
        self.endGameMenuButton.pack()

    def submit_char_event(self,event):
        self.submit_char()

    def submit_char(self):
        inp = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "")
        if len(inp) != 1:
            self.feedback.configure(text="Vous ne pouvez rentrer que une lettre!")
            return
        if not inp in ILib.allow_letters:
            self.feedback.configure(text="Cette lettre est invalide!")
            return
        if inp in self.log:
            self.feedback.configure(text="Cette lettre a déjà été utilisée!")
            return
        self.log.append(inp)
        self.clear = self.unClear(self.word,self.wordNoModify,self.clear,inp)
        if self.checkWin():
            print("win")
            if self.bestScore == -1:
                self.bestScore = self.errors
            elif self.bestScore > self.errors:
                self.bestScore = self.errors
            self.printEndMenu("Gagné")
            return
        self.wordLabel.configure(text=ILib.firstLetterCapital(self.clear))
        self.logLabel.configure(text=", ".join(self.log))

    def checkLoose(self):
        print("check loose")
        if self.errors >= self.maxErrors:
            print("Vous avez perdu ;( !")
            print("Le mot était " + ILib.firstLetterCapital(self.word) + "\n")
            return True
        return False

    def checkWin(self):
        if not "." in self.clear:
            print("*- "+ILib.firstLetterCapital(self.word)+" -*")
            print("Vous avez gagné :) !")
            return True
        return False

    def rejouer(self):
        self.menuFrame.pack_forget()
        self.endGameFrame.pack_forget()
        self.packGameWidgets()
        self.initGame()

    def retourMenu(self):
        self.endGameFrame.pack_forget()
        self.gameFrame.pack_forget()
        self.tk.unbind('<Return>')
        self.packMenu()

    def printEndMenu(self,message):
        self.menuFrame.pack_forget()
        self.gameFrame.pack_forget()
        self.tk.unbind('<Return>')
        self.packEndGameWidgets(message)

if __name__ == "__main__":
    app = App()
    app.tk.title("Pendu ;(")
    app.tk.mainloop()
