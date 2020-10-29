#!/usr/bin/env python

from tkinter import *
from collections import deque
import parser


# Main window
window_calculator = Tk()

window_calculator.title('Calculator')
window_calculator.geometry("450x370")

# Numbers entry
main_entry = Entry(window_calculator, font=("Calibri", 20))
main_entry.grid(row=0, column=0, columnspan=5, padx=30, pady=5)


i = 0
math_history = deque()

# Functions


def history(results):
    math_history.append(results)


def erase():
    main_entry.delete(0, END)


def show_history():
    if len(math_history):
        erase()
        main_entry.insert(0, math_history.pop())
    else:
        erase()
        main_entry.insert(0, "Error: No previous history")
        i = 0


def click_button_number(value):
    global i
    main_entry.insert(i, value)
    i += 1


def show_result():
    equation = main_entry.get()
    try:
        math_expression = parser.expr(equation).compile()
        result = eval(math_expression)
        erase()
        history(result)
        main_entry.insert(0, result)

        i = 0
    except:
        erase()
        main_entry.insert(0, "Math Error")
        i = 0


def undo():
    current_state = main_entry.get()
    if len(current_state):
        if "Error" in current_state:
            erase()
        else:
            undo_state = current_state[:-1]
            erase()
            main_entry.insert(0, undo_state)
    else:
        erase()


# Buttons Numbers
button_1 = Button(window_calculator, text="1", width=5,
                  height=2, command=lambda: click_button_number(1))
button_2 = Button(window_calculator, text="2", width=5,
                  height=2, command=lambda: click_button_number(2))
button_3 = Button(window_calculator, text="3", width=5,
                  height=2, command=lambda: click_button_number(3))
button_4 = Button(window_calculator, text="4", width=5,
                  height=2, command=lambda: click_button_number(4))
button_5 = Button(window_calculator, text="5", width=5,
                  height=2, command=lambda: click_button_number(5))
button_6 = Button(window_calculator, text="6", width=5,
                  height=2, command=lambda: click_button_number(6))
button_7 = Button(window_calculator, text="7", width=5,
                  height=2, command=lambda: click_button_number(7))
button_8 = Button(window_calculator, text="8", width=5,
                  height=2, command=lambda: click_button_number(8))
button_9 = Button(window_calculator, text="9", width=5,
                  height=2, command=lambda: click_button_number(9))
button_0 = Button(window_calculator, text="0", width=15,
                  height=2, command=lambda: click_button_number(0))

# Buttons for tools
button_del = Button(window_calculator, text="AC", width=5,
                    height=2, command=lambda: erase())
button_undo = Button(window_calculator, text="⌫", width=5,
                     height=2, command=lambda: undo())
button_p1 = Button(window_calculator, text="(", width=5,
                   height=2, command=lambda: click_button_number("("))
button_p2 = Button(window_calculator, text=")", width=5,
                   height=2, command=lambda: click_button_number(")"))
button_decimal = Button(window_calculator, text=".", width=5,
                        height=2, command=lambda: click_button_number("."))
button_history = Button(window_calculator, text="Ans",
                        width=5, height=2, command=lambda: show_history())


# Operators
button_div = Button(window_calculator, text="÷", width=5,
                    height=2, command=lambda: click_button_number("/"))
button_multiply = Button(window_calculator, text="×", width=5,
                         height=2, command=lambda: click_button_number("*"))
button_add = Button(window_calculator, text="+", width=5,
                    height=2, command=lambda: click_button_number("+"))
button_sustract = Button(window_calculator, text="-", width=5,
                         height=2, command=lambda: click_button_number("-"))
button_equal = Button(window_calculator, text="Intro", width=5,
                      height=6, command=lambda: show_result())
button_exponent = Button(window_calculator, text="EXP", width=5,
                         height=2, command=lambda: click_button_number("**"))
button_integer_division = Button(
    window_calculator, text="//", width=5, height=2, command=lambda: click_button_number("//"))

# Grid in screen
# First row
button_div.grid(row=1, column=3, padx=5, pady=5)
button_p1.grid(row=1, column=1, padx=5, pady=5)
button_p2.grid(row=1, column=2, padx=5, pady=5)
button_del.grid(row=1, column=0, padx=5, pady=5)
button_undo.grid(row=1, column=4, padx=5, pady=5)


# Second row
button_7.grid(row=2, column=0, padx=5, pady=5)
button_8.grid(row=2, column=1, padx=5, pady=5)
button_9.grid(row=2, column=2, padx=5, pady=5)
button_multiply.grid(row=2, column=3, padx=5, pady=5)
button_integer_division.grid(row=2, column=4, padx=5, pady=5)

# Third row
button_4.grid(row=3, column=0, padx=5, pady=5)
button_5.grid(row=3, column=1, padx=5, pady=5)
button_6.grid(row=3, column=2, padx=5, pady=5)
button_add.grid(row=3, column=3, padx=5, pady=5)
button_history.grid(row=3, column=4, padx=5, pady=5)

# Fourth row
button_1.grid(row=4, column=0, padx=5, pady=5)
button_2.grid(row=4, column=1, padx=5, pady=5)
button_3.grid(row=4, column=2, padx=5, pady=5)
button_sustract.grid(row=4, column=3, padx=5, pady=5)
button_equal.grid(row=4, column=4, rowspan=2, padx=5, pady=5)

# Fifth row
button_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
button_decimal.grid(row=5, column=2, padx=5, pady=5)
button_exponent.grid(row=5, column=3, padx=5, pady=5)

window_calculator.mainloop()
