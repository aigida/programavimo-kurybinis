from tkinter import *

# funkcija kuri sukuria mygtuko elementa ir jo vieta gride
def create_button(text, row, column, columnspan=1):
    button = Button(root,
                    text=text,
                    command=lambda: on_button_click(text),
                    height=2,
                    width=7)
    button.grid(row=row, column=column, columnspan=columnspan, sticky="EW")
    return button

def on_button_click(button_text):
    if button_text == "C":
        result.set("")
    elif button_text == "=":
      expression = result.get()
      result.set(eval(expression))
    else:
        result.set(result.get() + button_text)

root = Tk()
root.title("Calculator")
root.geometry("350x350")

result = StringVar()

entry = Entry(root,
              textvariable=result,
              width=20, 
              font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button1 = create_button("1", 1, 0)
button2 = create_button("2", 1, 1)
button3 = create_button("3", 1, 2)
button4 = create_button("4", 2, 0)
button5 = create_button("5", 2, 1)
button6 = create_button("6", 2, 2)
button7 = create_button("7", 3, 0)
button8 = create_button("8", 3, 1)
button9 = create_button("9", 3, 2)
button0 = create_button("0", 4, 1) 

button_add = create_button("+", 1, 3)
button_subtract = create_button("-", 2, 3)
button_multiply = create_button("*", 3, 3)
button_divide = create_button("/", 4, 3)

button_clear = create_button("C", 4, 0)
button_equals = create_button("=", 4, 2)

root.mainloop()
