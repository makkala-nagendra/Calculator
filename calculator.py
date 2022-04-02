from functools import *
from tkinter import *
from math import *
from matplotlib.axis import YAxis


number_pad = [
    ["7", "4", "1", ".", "√()"],
    ["8", "5", "2", "0", "%"],
    ["9", "6", "3", ",", "/"]]

bOperationsList = [["(", ")", "left", "right"],
                   ["*", "-", "+", "=" ]]

adOperationsList = [["sin()", "cos()", "tan()", "cot()", "sec()", "cosec()"],
                    ["sinh()", "cosh()", "tanh()", "coth()", "sech()", "cosech()"]]

adOperationsList2 = [["DEL","π", "log()", "log1p()", "log10()", "log2()"],
                     ["clear", "mod(a,b)", "pow(x,y)", "gcd(x,.)", "lcm(x,.)", "fact()"]]

mainRoot = Tk()
mainRoot.iconbitmap("myIcon.ico")
mainRoot.title("Calculator")
Grid.rowconfigure(mainRoot, 0, weight=1)
Grid.columnconfigure(mainRoot, 0, weight=1)

root = Frame(mainRoot)
root.grid(row=0, column=0, sticky=N+S+E+W)

def delDisplay():
    position = display.index(INSERT)
    s = display.get()
    display.delete(0, END)
    display.icursor(position -1)
    display.insert(0, s[:len(s)-1])

# left
def shift_cursor_left(event=None):
    position = display.index(INSERT)
    display.icursor(position - 1)

# right
def shift_cursor_right(event=None):
    position = display.index(INSERT)
    display.icursor(position + 1)


def modConveration(s):
    try:
        k = s.index("mod(")
        for i in range(k+len("mod("), len(s), 1):
            if(s[i] == ")"):
                l = i
                break
        sp = s[k+len("mod("):l].split(",")
        f1 = int(sp[0])/int(sp[1])
        f2 = floor(f1)*int(sp[1])
        res = int(sp[0])-f2
        s = s[:k]+str(res)+s[l+1:]
        return s
    except Exception as e:
        return s


def trignometricConverations(s='', v='', f1=None, f2=''):
    try:
        if f1 == None:
            f1 = "1"
        st = s.index(v)
        fn = 0
        for i in range(st+len(v), len(s), 1):
            if(s[i] == ")"):
                fn = i
                break
        k = s[st+len(v):fn]
        r = eval(f1+"/"+f2+"("+k+")")
        res = s[:st]+str(r)+s[fn+1:]
        return res
    except Exception as e:
        return s


def stringProcess():
    trig = [["cosech(", None, "sinh"],
            ["sech(", None, "cosh"],
            ["cosec(", None, "sin"],
            ["sec(", None, "cos"],
            ["coth(", None, "tanh"],
            ["cot(", None, "tan"]]

    s = display.get()

    for j in range(len(s)):
        try:
            for i in range(len(trig)):
                s = trignometricConverations(
                    s, trig[i][0], trig[i][1], trig[i][2])
        except:
            pass

    for i in range(len(s)):
        try:
            if(s.index("mod(") != None):
                s = modConveration(s)
                print(s)
        except:
            pass
    s = s.replace("√(", "sqrt(").replace("fact(", "factorial(")
    s = s.replace("π", "pi")
    return s


def cleareDisplay():
    display.delete(0, END)


def evluateInput():
    try:
        evluate_value = stringProcess()
        display.delete(0, END)
        r = eval(evluate_value)
        display.insert(0, r)
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Something wrong!")


def updateDisplay(s):
    if (display.get() == "Something wrong!"):
        display.delete(0, END)
    position = display.index(INSERT)
    evluate_value = display.get()
    display.delete(0, END)
    r = evluate_value[:position]+s+evluate_value[position:]
    display.insert(0, r)
    if(position != 0):
        display.icursor(position+1)
        display.xview(position-3)
    else:
        #position = len(r)
        display.icursor(position+1)


def numPad():
    for i in range(len(number_pad)):
        Grid.columnconfigure(root, i, weight=1)
        for j in range(len(number_pad[i])):
            Grid.rowconfigure(root, j+2, weight=1)
            Button(root, text=number_pad[i][j], font=("Arial", 15), command=partial(
                updateDisplay, number_pad[i][j])).grid(column=i, row=j+2, sticky=N+S+E+W)


def BasicOperations():
    for i in range(len(bOperationsList)):
        Grid.rowconfigure(root, i+1, weight=1)
        if(i == 0):
            for j in range(len(bOperationsList[i])):
                Grid.columnconfigure(root, j, weight=1)
                if(bOperationsList[i][j] == "clear"):
                    Button(root, text=bOperationsList[i][j], font=(
                        "Arial", 15), command=cleareDisplay, height=3, width=6).grid(column=j, row=i+1, sticky=N+S+E+W)
                elif(bOperationsList[i][j] == "left"):
                    Button(root, text=bOperationsList[i][j], font=("Arial", 15), command=shift_cursor_left,
                           height=3, width=6).grid(column=j, row=i+1, sticky=N+S+E+W)
                elif(bOperationsList[i][j] == "right"):
                    Button(root, text=bOperationsList[i][j], font=("Arial", 15), command=shift_cursor_right,
                           height=3, width=6).grid(column=j, row=i+1, sticky=N+S+E+W)
                else:
                    Button(root, text=bOperationsList[i][j], font=("Arial", 15), command=partial(
                        updateDisplay, bOperationsList[i][j]), height=3, width=6).grid(column=j, row=i+1, sticky=N+S+E+W)
        else:
            for j in range(len(bOperationsList[i])):
                if(bOperationsList[i][j] == "clear"):
                    Button(root, text=bOperationsList[i][j], font=(
                        "Arial", 15), command=cleareDisplay, height=3, width=6).grid(column=i+2, row=j+2, sticky=N+S+E+W)
                elif(bOperationsList[i][j] != "="):
                    Button(root, text=bOperationsList[i][j], font=("Arial", 15), command=partial(
                        updateDisplay, bOperationsList[i][j]), height=3, width=6).grid(column=i+2, row=j+2, sticky=N+S+E+W)
                else:
                    Button(root, text=bOperationsList[i][j], font=(
                        "Arial", 15), command=evluateInput, height=3, width=6).grid(column=i+2, row=j+2, rowspan=2,
                                                                                    sticky=N+S+E+W)


def AdvanceOperations():
    for i in range(len(adOperationsList)):
        Grid.columnconfigure(root, i+4, weight=1)
        for j in range(len(adOperationsList[i])):
            Grid.rowconfigure(root, j+1, weight=1)
            Button(root, text=adOperationsList[i][j], font=("Arial", 15),
                   command=partial(updateDisplay, adOperationsList[i][j]),
                   height=3, width=6).grid(column=i+4, row=j+1, sticky=N+S+E+W)


def AdvanceOperations2():
    for i in range(len(adOperationsList2)):
        Grid.columnconfigure(root, i+6, weight=1)
        for j in range(len(adOperationsList2[i])):
            Grid.rowconfigure(root, j+1, weight=1)
            if(adOperationsList2[i][j] == "clear"):
                Button(root, text=adOperationsList2[i][j], font=(
                    "Arial", 15), command=cleareDisplay, height=3, width=6).grid(column=i+6, row=j+1, sticky=N+S+E+W)
            elif(adOperationsList2[i][j] == "DEL"):
                Button(root, text=adOperationsList2[i][j], font=(
                    "Arial", 15), command=delDisplay, height=3, width=6).grid(column=i+6, row=j+1, sticky=N+S+E+W)
            else:
                Button(root, text=adOperationsList2[i][j], font=("Arial", 15),
                       command=partial(updateDisplay, adOperationsList2[i][j]),
                       height=3, width=6).grid(column=i+6, row=j+1, sticky=N+S+E+W)


scrollbar = Scrollbar(orient=HORIZONTAL)
display = Entry(root, width=30, highlightthickness=4,
                font=("Arial", 30), xscrollcommand=scrollbar.set)
display.grid(row=0, columnspan=8, sticky=N+S+E+W)
scrollbar.config(command=display.xview)
scrollbar.grid(row=1, columnspan=6, sticky=N+S+E+W)
display.config()

numPad()
BasicOperations()
AdvanceOperations()
AdvanceOperations2()
root.mainloop()