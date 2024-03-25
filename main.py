import os
import sys

sys.path.append('app')

from app.Calculator import CalculatorApp 
import tkinter as tk


def main():
    root = tk.Tk()
    app = CalculatorApp(root)          #create an instance of the Calculator class, which will implicity call its __init__ method
    root.mainloop()

if __name__ == "__main__":
    main()