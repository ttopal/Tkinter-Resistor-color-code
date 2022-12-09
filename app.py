# starting point of the program
import tkinter as tk
import tkinter.ttk as ttk

# internals
from widgets.rescode import ResCode

class Applications():
    def __init__(self, master):
        
        base = ResCode(master)
        base.pack(expand=True, fill="both")

        master.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("690x500")
    window.title("Taner TOPAL Tkinter Resistor Color Code")
    app = Applications(window)