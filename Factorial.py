from tkinter import ttk
import tkinter as tk

from Functions import File_choice
from Functions import About_Window
from Functions import GitHub

# Main window

Main = tk.Tk()
Main.geometry ("900x600")
Main.title ("Factorial [Preview]")
Main.configure (bg = 'white')
Main.resizable (False, False)

# Buttons

#! Open Button

Open_Button = ttk.Button (text = "Open", command = File_choice)
Open_Button.place (x = 550, y = 150, width = 295, height = 75)

#! GitHub Button

GitHub_Button = ttk.Button (text = "GitHub", command = GitHub)
GitHub_Button.place (x = 550, y = 250, width = 295, height = 75)

#! About Button

About_Button = ttk.Button (text = "About", command = About_Window)
About_Button.place (x = 550, y = 350, width = 295, height = 75)

# Labels

L1 = tk.Label (text = "Factorial", font = ("Montserrat Bold", 35), bg = 'white')
L1.place (x = 160, y = 200)

L2 = tk.Label (text = "[ ! ] Preview Build", font = ("Montserrat Medium", 18), bg = 'white')
L2.place (x = 160, y = 270)

Main.mainloop ()