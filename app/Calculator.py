import sys
sys.path.append('Operations')


import tkinter as tk
from Operations.addition import add
from Operations.soustraction import subtract
from Operations.multiplication import multiply
from Operations.division import divide

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 18), bd=10, insertwidth=3, width=20, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            if text == '=':
                button = tk.Button(self.root, text=text, font=('Arial', 18), padx=40, pady=20, command=self.calculate)
            elif text == 'C':
                button = tk.Button(self.root, text=text, font=('Arial', 18), padx=40, pady=20, command=self.clear_entry)
            else:
                button = tk.Button(self.root, text=text, font=('Arial', 18), padx=40, pady=20, command=lambda t=text: self.update_entry(t))
            button.grid(row=row, column=column)

    def update_entry(self, value):
        current_text = self.result_var.get()
        if current_text == "Error":
            current_text = ""
        self.result_var.set(current_text + value)

    def clear_entry(self):
        self.result_var.set("")

    def calculate(self):
        try:
            expression = self.result_var.get()
            result = eval(expression)  # Directly evaluating expression (insecure in uncontrolled environments)
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
