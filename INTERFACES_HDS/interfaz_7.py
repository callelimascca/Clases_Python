from tkinter import *
ventana = Tk() 
ventana.title("Calculadora básica")
ventana.config(bg="#54ABC2")

result = StringVar()
entry = Entry(ventana, textvariable=result)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
entry.config(bg = "#87E5F0")
def add_number(number):
    current = result.get()
    result.set(current + number)

def borrar():
	entry.delete(0, END)

    
button1 = Button(ventana, text="1", command=lambda:add_number("1"))
button2 = Button(ventana, text="2", command=lambda:add_number("2"))
button3 = Button(ventana, text="3", command=lambda:add_number("3"))
button4 = Button(ventana, text="4", command=lambda:add_number("4"))
button5 = Button(ventana, text="5", command=lambda:add_number("5"))
button6 = Button(ventana, text="6", command=lambda:add_number("6"))
button7 = Button(ventana, text="7", command=lambda:add_number("7"))
button8 = Button(ventana, text="8", command=lambda:add_number("8"))
button9 = Button(ventana, text="9", command=lambda:add_number("9"))
button0 = Button(ventana, text="0", command=lambda:add_number("0"))
button_suma = Button(ventana, text="+", command=lambda:add_number("+"))
button_resta = Button(ventana, text="-", command=lambda:add_number("-"))
button_multiplicar = Button(ventana, text="*", command=lambda:add_number("*"))
button_divide = Button(ventana, text="/", command=lambda:add_number("/"))
button_igual = Button(ventana, text="=", command=lambda:result.set(eval(result.get())))
boton_borrar = Button(ventana, text = "CLEAR", width= 10, height = 1, command = lambda: borrar())

button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
button9.grid(row=1, column=2, padx=5, pady=5)
button_divide.grid(row=1, column=3, padx=5, pady=5)
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
button_multiplicar.grid(row=2, column=3, padx=5, pady=5)
button1.grid(row=3, column=0, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=3, column=2, padx=5, pady=5)
button_resta.grid(row=3, column=3, padx=5, pady=5)
button0.grid(row=4, column=0, padx=5, pady=5)
button_igual.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
button_suma.grid(row=4, column=3, padx=5, pady=5)
boton_borrar.grid(row=5, column =0, columnspan=4)
ventana.mainloop()


