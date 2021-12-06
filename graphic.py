import tkinter as tk
import ILib
# import App

# if __name__ == "__main__":
#     app = App.App()
#     app.title("Pendu ;(")
#     app.mainloop()

TKI_Principal = tk.Tk ( )

IMG_Image = tk.PhotoImage ( file = "img/bonhomme1.gif" )

IMG_Image = tk.PhotoImage(file = "img/bonhomme1.gif")
canvas = tk.Canvas(TKI_Principal, bg = "white" , width = 1000, height = 500)
temp = canvas.create_image(50,10, image = IMG_Image ,  anchor = "nw")
canvas.pack(side = "right")

TKI_Principal.mainloop ( )
