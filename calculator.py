import PySimpleGUI as sg
import math

calc_buttons = [
    ["AC", "←", "√", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "±", "="]
    ]

font = ("Yu Gothic UI", 20)
layout = [
    [sg.Text("0",
             key="-output-",
             background_color="white", text_color="black",
             font=font,
             expand_x=True)],
    ]

for row in calc_buttons:
    buttons = []
    for ch in row:
        btn = sg.Button(
            ch,
            key=f"-btn{ch}",
            size=(3, 1),
            font=font,
        )
        buttons.append(btn)
    layout.append(buttons)

window = sg.Window("電卓", layout)
output = "0"

while True:
    event, _ = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event.startswith("-btn"):
        ch = window[event].GetText()
        if output == "0" or output.startswith("E:"):
            output = ""
        if ch == "AC":
            output = "0"
        elif ch == "←":
            output = output[:-1]
        elif ch == "√":
            output = str(math.sqrt(float(output)))
        elif ch == "±":
            try:
                output = str(-float(output))
            except ValueError:
                pass
        elif ch == "=":
            try:
                expression = output.replace("÷", "/")
                expression = expression.replace("×", "*")
                output = str(eval(expression))
            except Exception as e:
                output = "E:" + str(e)
        else:
            output += ch
        window["-output-"].update(output)

window.close()
