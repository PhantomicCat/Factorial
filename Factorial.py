from tkinter import ttk
import tkinter as tk

from Functions import File_choice
from Functions import About_Window
from Functions import GitHub
from Functions import Editor

# Main window

Main = tk.Tk()
Main.geometry ("900x600")
Main.title ("Factorial [Preview]")
Main.configure (bg = 'white')
Main.resizable (False, False)

# Buttons

#! Open Button

Open_Button = ttk.Button (text = "Open", command = File_choice)
Open_Button.place (x = 550, y = 100, width = 295, height = 75)

#! GitHub Button

GitHub_Button = ttk.Button (text = "GitHub", command = GitHub)
GitHub_Button.place (x = 550, y = 300, width = 295, height = 75)

#! About Button

About_Button = ttk.Button (text = "About", command = About_Window)
About_Button.place (x = 550, y = 400, width = 295, height = 75)

#! Editor Button
Editor_Button = ttk.Button (text = "Editor (In Development)", command = Editor)
Editor_Button.place (x = 550, y = 200, width = 295, height = 75)

# Labels

L1 = tk.Label (text = "Factorial", font = ("Montserrat Bold", 35), bg = 'white')
L1.place (x = 160, y = 200)

L2 = tk.Label (text = "[ ! ] Preview Build", font = ("Montserrat Medium", 18), bg = 'white')
L2.place (x = 160, y = 270)

Version = tk.Label (text = "Version 0.1.1 Preview", font = ("Montserrat Medium", 10), bg = 'white')
Version.place (y = 575, x = 755)

Main.mainloop ()