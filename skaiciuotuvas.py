from tkinter import *
from tkinter import colorchooser #importinau colorchooseri is tknt
import math #importinau matematikos tokia kaip ir funkcija
import locale
locale.setlocale(locale.LC_ALL, 'en_EN')

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
    elif button_text == "=": #gerai sita darau nakti ir irgi panaudojau chatgpt nes maisos smegenys, bet cia panaudojau locale module
      expression = result.get()
      result.set(locale.format_string("%.2f", eval(expression)))
    elif button_text == "Color": #visas sitas elif kai paspaudziu color button
        color = colorchooser.askcolor()[1] #askcolor colorshooser paima moduli is tkinter, [1] yra hexademical sistema naudojama dizainams dazniausiai(nlb zinau ka reiskia lygtais kaip visi tie #fffff spalvu dalykai RGB sistemoj)
        root.config(bg=color)  
    elif button_text == "sin":
        expression = result.get()
        result.set(math.sin(eval(expression))) #cia yra is to math paimta funkcija su sinusais/cos/tg
    elif button_text == "cos":
        expression = result.get()
        result.set(math.cos(eval(expression)))
    elif button_text == "tan":
        expression = result.get()
        result.set(math.tan(eval(expression)))
    elif "%" in result.get():  #niekaip nesupratau kaip su procentais daryt ir vis man nesigavo tai su chatgpt padariau, bet ir tai kokia valanda su tuo vargau
        expression = result.get().replace("%", "")
        if button_text is not None:
            result.set(str(eval(expression)/100 * float(button_text)))
        else:
            result.set("")
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
button_dot = create_button(".", 5, 1)

button_add = create_button("+", 1, 3)
button_subtract = create_button("-", 2, 3)
button_multiply = create_button("*", 3, 3)
button_divide = create_button("/", 4, 3)

button_clear = create_button("C", 4, 0)
button_equals = create_button("=", 4, 2)

#prideti buttonai:
button_sin = create_button("sin", 1, 4)
button_cos = create_button("cos", 2, 4)
button_tan = create_button("tan", 3, 4)
button_percentage = create_button("%", 4, 4)

button_colorpicker = create_button("Color", 5, 0) 


root.mainloop()
