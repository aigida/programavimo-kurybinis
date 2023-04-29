from tkinter import *
from tkinter import colorchooser
import math
import locale
from decimal import Decimal
locale.setlocale(locale.LC_ALL, 'en_EN')

MAX_CHARS = 20

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
        try:
            result_value = eval(expression)
            if "." not in expression:
                result_value = int(result_value)
            if isinstance(result_value, float) and math.isnan(result_value):
                raise ValueError("Not a number")
            if isinstance(result_value, float) and math.isinf(result_value):
                raise ValueError("Infinity")
            if isinstance(result_value, float) and math.isinf(-result_value):
                raise ValueError("-Infinity")
            result.set(str(result_value))
        except (SyntaxError, ZeroDivisionError, ValueError):
            result.set("Error")
    elif button_text == "Color":
        color = colorchooser.askcolor()[1]
        root.config(bg=color)
    elif button_text == "sin":
        expression = result.get()
        angle = math.radians(eval(expression))
        sin_value = math.sin(angle)
        if math.isclose(sin_value, 0, rel_tol=1e-9, abs_tol=1e-9):
            result.set("0")
        else:
            result.set(str(sin_value))
    elif button_text == "cos":
        expression = result.get()
        angle = math.radians(eval(expression))
        if angle % (math.pi / 2) == 0: 
            result.set(round(math.cos(angle)))
        else:
            result.set(round(math.cos(angle), 10))
    elif button_text == "tan":
        expression = result.get()
        angle_deg = eval(expression)
        if angle_deg % 180 == 0:
            result.set("0")
        elif angle_deg % 90 == 0:
            result.set("Error")
        else:
            angle_rad = math.radians(angle_deg)
            result_value = math.tan(angle_rad)
            if math.isclose(result_value, 0, rel_tol=1e-9, abs_tol=1e-9):
                result.set("0")
            else:
                result.set(str(result_value))


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
    elif button_text.lower() == "in to cm":
        inches_to_centimeters()
    elif button_text.lower() == "cm to m":
        centimeters_to_meters()
    elif button_text.lower() == "cm2 to m2":
        cm2_to_m2()
    elif button_text.lower() == "g to kg":
        g_to_kg()
    elif button_text.lower() == "ml to l":
        ml_to_l()
    elif button_text.lower() == "sqrt":
        expression = result.get()
        result.set(math.sqrt(eval(expression)))
    elif button_text.lower() == "cbrt":
        expression = result.get()
        result.set(math.pow(eval(expression), 1/3))
    elif button_text == "π":
        result.set(str(math.pi))
    elif button_text.lower() == "e":
        result.set(str(math.e))
    elif button_text == "^2":
        square()
    elif button_text == "^3":
        cube()
    elif button_text == "n!":
        expression = result.get()
        n = int(eval(expression))
        if n < 0:
            result.set("Error")
        else:
            decimal_n = Decimal(n)
            decimal_factorial = Decimal(math.factorial(min(n, 4300)))
            if len(str(decimal_factorial)) > 4300:
                result.set("Error")
            else:
                result.set(str(decimal_factorial))
    else:
        result.set(result.get() + button_text)
        



def change_button_color(color):
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0,
                   button_dot, button_add, button_subtract, button_multiply, button_divide, button_clear,
                   button_equals, button_sin, button_cos, button_tan, button_percentage, button_colorpicker, button_cf]:
        button.config(bg=color)

def logarithm_base_10():
    expression = result.get()
    result.set(math.log10(eval(expression)))

def inches_to_centimeters():
    expression = result.get()
    try:
        inches = float(expression)
    except ValueError:
        result.set("Error")
        return
    centimeters = inches * 2.54
    if abs(centimeters) < 10**9:
        result.set(str(centimeters))
    else:
        result.set(f"{centimeters:.2e}")

def centimeters_to_meters():
    expression = result.get()
    try:
        centimeters = float(expression)
    except ValueError:
        result.set("Error")
        return
    meters = centimeters * 0.01
    if abs(meters) < 10**9:
        result.set(str(meters))
    else:
        result.set(f"{meters:.2e}")

def cm2_to_m2():
    expression = result.get()
    try:
        cm2 = float(expression)
    except ValueError:
        result.set("Error")
        return
    m2 = cm2 / 10000
    if abs(m2) < 10**9:
        result.set(str(m2))
    else:
        result.set(f"{m2:.2e}")

def g_to_kg():
    expression = result.get()
    try:
        g = float(expression)
    except ValueError:
        result.set("Error")
        return
    kg = g / 1000
    if abs(kg) < 10**9:
        result.set(str(kg))
    else:
        result.set(f"{kg:.2e}")

def ml_to_l():
    expression = result.get()
    try:
        ml = float(expression)
    except ValueError:
        result.set("Error")
        return
    l = ml / 1000
    if abs(l) < 10**9:
        result.set(str(l))
    else:
        result.set(f"{l:.2e}")

def square():
    current_value = float(result.get())
    result.set(str(current_value ** 2))

def cube():
    expression = result.get()
    result.set(eval(expression)**3)


root = Tk()
root.title("Calculator")
root.geometry("264x254")

result = StringVar()

def validate_entry(text):
    allowed = set("0123456789+-*/().")
    return set(text).issubset(allowed)

vcmd = (root.register(validate_entry), '%S')

entry = Entry(root, textvariable=result, width=20, font=("Arial", 16), validate="key", validatecommand=vcmd)
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
button_percentage = create_button("%", 4, 2, button_color="light green")

button_clear = create_button("C", 4, 0, button_color="orange")
button_equals = create_button("=", 5, 2, button_color="orange")

button_sin = create_button("sin", 1, 4, button_color="pink")
button_cos = create_button("cos", 2, 4, button_color="pink")
button_tan = create_button("tan", 3, 4, button_color="pink")
button_log = create_button("log10", 4, 4, button_color="pink")
button_pi = create_button("π", 6, 1, button_color="pink")
button_e = create_button("e", 6, 2, button_color="pink")
button_number1 = create_button("^2", 6, 3, button_color="pink")
button_number2 = create_button("^3", 6, 4, button_color="pink")
button_cf = create_button("C to F", 5, 4, button_color="pink")
button_fct = create_button("n!", 6, 0, button_color="pink")

button_sqrt = create_button("sqrt", 7, 0, button_color="medium orchid")
button_cbrt = create_button("cbrt", 7, 1, button_color="medium orchid")

button_colorpicker = create_button("Color", 5, 0, button_color="grey")



def expand_contract():
    global is_expanded
    if is_expanded:
        root.geometry("264x254")
        is_expanded = False
    else:
        root.geometry("325x380")
        is_expanded = True
        
button_expand = create_button("Expand", 5, 3, button_color="orange")
 
button_expand.config(command=expand_contract)

is_expanded = False

button_in_cm = create_button("In to Cm", 8, 0, button_color="indian red")
button_cm_m = create_button("Cm to m", 8, 1, button_color="indian red")
button_cm2_m2 = create_button("Cm2 to m2", 8, 2, button_color="indian red")
button_g_kg = create_button("g to kg", 8, 3, button_color = "indian red")
button_ml_l = create_button("ml to l", 8, 4, button_color="indian red")


root.mainloop()