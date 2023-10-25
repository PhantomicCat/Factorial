from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkfont
import webbrowser

def File_choice():
    file_path = filedialog.askopenfilename()

    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()

        read_window = tk.Tk()
        read_window.geometry("900x500")
        read_window.resizable (False, False)
        read_window.title("Factorial [Reader]")
        read_window.configure (bg = 'white')

        read_text = tk.Text (read_window, width = 500, height = 200, font = ("Montserrat Bold", 12))
        read_text.configure (bg = 'white')
        read_text.pack()

        def Increase_Font_Size ():
            current_font = read_text['font']  
            font_size = tkfont.Font(font=current_font).actual()['size']
            new_font_size = font_size + 2
            read_text.configure(font=(current_font, new_font_size))

        def Decrease_Font_Size ():
            current_font = read_text['font']
            font_size = tkfont.Font(font=current_font).actual()['size']
            new_font_size = font_size - 2 
            read_text.configure(font=(current_font, new_font_size))

        Font_Size_Button1 = ttk.Button (read_window, text = "Increase size", command = Increase_Font_Size)
        Font_Size_Button1.place (x = 600, y = 400, width = 130, height = 75)

        Font_Size_Button2 = ttk.Button (read_window, text = "Decrease font", command = Decrease_Font_Size)
        Font_Size_Button2.place (x = 450, y = 400, width = 130, height = 75)

        read_text.insert(tk.END, file_content)
        read_text.configure(state="disabled")

        def Coping ():
            read_window.clipboard_clear ()
            read_window.clipboard_append (file_content)

        Copy_Button = ttk.Button (read_window, text = "Copy", command = Coping)
        Copy_Button.place (x = 750, y = 400, width = 130, height = 75)

    else:
        messagebox.showerror ("Factorial [Reader]", "You may not have selected a file in File Explorer. Try opening the file again.")

def GitHub ():
    webbrowser.open ("https://github.com/PhantomicCat/Factorial")

def About_Window ():
    About = tk.Tk()
    About.configure (bg = 'white')
    About.geometry ("725x350")
    About.title ("About Program")
    About.resizable (False, False)

    # Labels

    L1 = tk.Label (About, text = 'Factorial', font = ("Montserrat Bold", 25), bg = 'white')
    L1.pack (pady = 5)

    L2 = tk.Label (About, text = '[ ! ] Preview Build', font = ("Montserrat Medium", 14), bg = 'white')
    L2.pack (pady = 1)

    L3 = tk.Label (About, text = 'This is Preview version of Factorial. Most features can be changed, added or removed.', font = ("Montserrat Medium", 10), bg = 'white')
    L3.pack (pady = 10)

    L3_2 = tk.Label (About, text = 'The program may contain bugs at this stage of development', font = ("Montserrat Medium", 10), bg = 'white')
    L3_2.pack ()

    L4 = tk.Label (About, text = "Created by PhantomicCat", font = ("Montserrat Bold", 15), bg = "white")
    L4.pack (pady = 60)

    L5 = tk.Label (About, text = "This app is just for fun, so if you want to modify it to suit your needs (Or even improve it), just Fork the project's GitHub page.", font = ("Montserrat Medium", 8), bg = 'white')
    L5.place (x = 5, y = 320)

    About.mainloop ()