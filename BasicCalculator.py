from tkinter import *
import parser
root = Tk()
root.title("Martin's Calculator")
# root.geometry("500x500")
root.configure(background = 'Blue')

i = 0


def clear_all():
    """clears all the content in the Entry widget"""
    txtDisplay.delete(0, END)


def variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i
    txtDisplay.insert(i, num)
    i += 1


def operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    txtDisplay.insert(i,operator)
    i += length


def equalsNumber():
    whole_string = txtDisplay.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        txtDisplay.insert(0, result)
    except Exception:
        clear_all()
        txtDisplay.insert(0, "Error!")



frame = Frame(root)
frame.pack()

textEntry = StringVar()
txtDisplay = Entry(frame,textvariable = textEntry,bd = 20, insertwidth = 1,font = 30)
txtDisplay.pack(side = TOP)

topFrame = Frame(root)
topFrame.pack(side = TOP)

num1 = Button(topFrame,padx = 16,pady = 16,bd = 8, text = "1",fg = "black",background = 'yellow',command = lambda : variables(1))
num1.pack(side = LEFT)
num2 = Button(topFrame,padx = 16,pady = 16,bd = 8, text = "2",fg = "black",background = 'yellow',command = lambda : variables(2))
num2.pack(side = LEFT)
num3 = Button(topFrame,padx = 16,pady = 16,bd = 8, text = "3",fg = "black",background = 'yellow',command = lambda : variables(3))
num3.pack(side = LEFT)
num4 = Button(topFrame,padx = 16,pady = 16,bd = 8, text = "4",fg = "black",background = 'yellow',command = lambda : variables(4))
num4.pack(side = LEFT)
num5 = Button(topFrame,padx = 16,pady = 16,bd = 8, text = "5",fg = "black",background = 'yellow',command = lambda : variables(5))
num5.pack(side = LEFT)

secondFrame = Frame(root)
secondFrame.pack(side = TOP)

num6 = Button(secondFrame,padx = 16,pady = 16,bd = 8, text = "6",fg = "black",background = 'yellow',command = lambda : variables(6))
num6.pack(side = LEFT)
num7 = Button(secondFrame,padx = 16,pady = 16,bd = 8, text = "7",fg = "black",background = 'yellow',command = lambda : variables(7))
num7.pack(side = LEFT)
num8 = Button(secondFrame,padx = 16,pady = 16,bd = 8, text = "8",fg = "black",background = 'yellow',command = lambda : variables(8))
num8.pack(side = LEFT)
num9 = Button(secondFrame,padx = 16,pady = 16,bd = 8, text = "9",fg = "black",background = 'yellow',command = lambda : variables(9))
num9.pack(side = LEFT)
num0 = Button(secondFrame,padx = 16,pady = 16,bd = 8, text = "0",fg = "black",background = 'yellow',command = lambda : variables(0))
num0.pack(side = LEFT)

thirdFrame = Frame(root)
thirdFrame.pack(side = TOP)

numPlus = Button(thirdFrame,padx = 16,pady = 16,bd = 8, text = "+",fg = "black",background = 'yellow',command = lambda : operation("+"))
numPlus.pack(side = LEFT)
numMinus = Button(thirdFrame,padx = 16,pady = 16,bd = 8, text = "-",fg = "black",background = 'yellow',command = lambda : operation("-"))
numMinus.pack(side = LEFT)
numMultiply = Button(thirdFrame,padx = 16,pady = 16,bd = 8, text = "*",fg = "black",background = 'yellow',command = lambda : operation("*"))
numMultiply.pack(side = LEFT)
numDivide = Button(thirdFrame,padx = 16,pady = 16,bd = 8, text = "/",fg = "black",background = 'yellow',command = lambda : operation("/"))
numDivide.pack(side = LEFT)
numEquals = Button(thirdFrame,padx = 16,pady = 16,bd = 8, text = "=",fg = "black",background = 'yellow',command = equalsNumber)
numEquals.pack(side = LEFT)
clearScreen = Button(thirdFrame,padx = 16,pady = 16,bd = 8, text = "AC",fg = "black",background = 'yellow',command = clear_all)
clearScreen.pack(side = LEFT)

root.mainloop()