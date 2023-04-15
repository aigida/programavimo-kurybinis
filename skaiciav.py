from tkinter import *
from tkinter import colorchooser #importinau colorchooseri is tknt
import math#importinau matematikos tokia kaip ir funkcija
import locale
locale.setlocale(locale.LC_ALL, 'en_EN')

def create_button(text, row, column, columnspan=1, button_color="white"):
    button = Button(root,
                    text=text,
                    command=lambda: on_button_click(text),
                    height=2,
                    width=7,
                    bg=button_color,
                    fg="black"
                    )
    button.grid(row=row, column=column, columnspan=columnspan, sticky="EW")
    return button

def on_button_click(button_text):
    if button_text == "C":
        result.set("")
    elif button_text == "=":
        expression = result.get()
        result.set(locale.format_string("%.2f", eval(expression)))
    elif button_text == "Color":
        color = colorchooser.askcolor()[1]
        root.config(bg=color) #nereikia tos papildomos eilutes ten kur pridejai tada islieka tos pacios spalvos buttonu ir nesikeicia kartu su fonu
    elif button_text == "sin":
        expression = result.get()
        result.set(math.sin(eval(expression)))
    elif button_text == "cos":
        expression = result.get()
        result.set(math.cos(eval(expression)))
    elif button_text == "tan":
        expression = result.get()
        result.set(math.tan(eval(expression)))
    elif "%" in result.get():
        expression = result.get().replace("%", "")
        if button_text is not None:
            result.set(str(eval(expression)/100 * float(button_text)))
        else:
            result.set("")
    elif button_text == "log10":
        logarithm_base_10()
    elif button_text == "C to F":
        celsius = float(result.get())
        fahrenheit = (celsius * 9/5) + 32
        result.set(locale.format_string("%.2f", fahrenheit))
    else:
        result.set(result.get() + button_text)



def change_button_color(color): #cia kazkoks loopas kur keicia spalvas (gal rasti koki sutrumpinta buda?)
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0,
                   button_dot, button_add, button_subtract, button_multiply, button_divide, button_clear,
                   button_equals, button_sin, button_cos, button_tan, button_percentage, button_colorpicker, button_cf]:
        button.config(bg=color)

def logarithm_base_10():
    expression = result.get()
    result.set(math.log10(eval(expression)))

root = Tk()
root.title("Calculator")
root.geometry("264x254")

result = StringVar()

entry = Entry(root,
              textvariable=result,
              width=20, 
              font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button1 = create_button("1", 1, 0, button_color="light blue")
button2 = create_button("2", 1, 1, button_color="light blue")
button3 = create_button("3", 1, 2, button_color="light blue")
button4 = create_button("4", 2, 0, button_color="light blue")
button5 = create_button("5", 2, 1, button_color="light blue")
button6 = create_button("6", 2, 2, button_color="light blue")
button7 = create_button("7", 3, 0, button_color="light blue")
button8 = create_button("8", 3, 1, button_color="light blue")
button9 = create_button("9", 3, 2, button_color="light blue")
button0 = create_button("0", 4, 1, button_color="light blue")
button_dot = create_button(".", 5, 1, button_color="light blue")

button_add = create_button("+", 1, 3, button_color="light green")
button_subtract = create_button("-", 2, 3, button_color="light green")
button_multiply = create_button("*", 3, 3, button_color="light green")
button_divide = create_button("/", 4, 3, button_color="light green")
button_percentage = create_button("%", 5, 2, button_color="light green")

button_clear = create_button("C", 4, 0, button_color="orange")
button_equals = create_button("=", 4, 2, button_color="orange")

button_sin = create_button("sin", 1, 4, button_color="pink")
button_cos = create_button("cos", 2, 4, button_color="pink")
button_tan = create_button("tan", 3, 4, button_color="pink")
button_log = create_button("log10", 4, 4, button_color="pink")

button_cf = create_button("C to F", 5, 4, button_color="pink")

button_colorpicker = create_button("Color", 5, 0, button_color="grey")

def expand_contract():
    global is_expanded
    if is_expanded:
        root.geometry("264x254")
        is_expanded = False
    else:
        root.geometry("324x350")
        is_expanded = True
        
button_expand = create_button("Expand", 5, 3, button_color="orange")
button_expand.config(command=expand_contract)

is_expanded = False


root.mainloop()