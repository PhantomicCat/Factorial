import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def Editor ():

    Editor_Window = tk.Tk ()
    Editor_Window.configure (bg = 'white')
    Editor_Window.title ("Factorial Editor")
    Editor_Window.geometry ("1000x650")

    Text_Box = tk.Text (Editor_Window, width = 100, font = ("Montserrat Bold", 12))
    Text_Box.pack ()

    def Saving():
        BN = Text_Box.get("1.0", tk.END)

        filetypes = (
            ('Text Documents', '*.txt'),
            ('All Files', '*.*')
        )
        
        file_path = filedialog.asksaveasfilename(filetypes= filetypes)

        with open(file_path, "w") as file:
         file.write(BN)

    Save_button = ttk.Button (Editor_Window, text = "Save", command = Saving)

    Save_button.place (x = 850, y = 550, width = 130, height = 75)

    Editor_Window.mainloop ()