from tkinter import *

ventana = Tk()
ventana.title("calculadora")

i = 0

#entrada
e_texto = Entry(ventana, font = ("Arial 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady=5)

#Cambio de color de botones 

import random


def changeBG():
    ventana.config(backgrond = 'green')
    colors =["pink", "yellow", "black", "green", "purple", "red", "gray"]
    random_colors = random.choice(colors)
    ventana.config(background = random_colors)
    
#Funciones

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i = 0
    
def back():
    global i
    i = i-1
    e_texto.delete(i, END)
    
def hacer_operacion():
    ecuacion = e_texto.get()
    #Reemplazar 'i' con 'j' para numeros complejos y evaluar
    ecuacion = ecuacion.replace('i', 'j')
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i = 0   
    
def Cambio():
    if (boton_ON[ 'text'] == 'ON'):
        boton_ON[ 'text'] = 'OFF'
    else:
        boton_ON[ 'text'] = 'ON'   
        
        if (boton1[ 'state'] == NORMAL):
            boton1[ 'state'] = DISABLED
        else:
            boton1['state'] = NORMAL
            
        if (boton2[ 'state'] == NORMAL):
            boton2[ 'state'] = DISABLED
        else:
            boton2['state'] = NORMAL
            
        if (boton3[ 'state'] == NORMAL):
            boton3[ 'state'] = DISABLED
        else:
            boton3['state'] = NORMAL
            
        if (boton4[ 'state'] == NORMAL):
            boton4[ 'state'] = DISABLED
        else:
            boton4['state'] = NORMAL
            
ventana.configure (background='navy')
   
#Botones

boton1 = Button(ventana, text = "1", width = 5, height = 2, state=DISABLED, activebackground= 'yellow', command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, state=DISABLED, activebackground= 'green', command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, state=DISABLED, activebackground= 'blue', command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, state=DISABLED, activebackground= 'red', command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, activebackground= 'orange', command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, activebackground= 'purple', command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, activebackground= 'brown', command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, activebackground= 'pink', command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, activebackground= 'violet', command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 13, height = 2, activebackground= 'grey', command = lambda: click_boton(0))

boton_borrar = Button(ventana, text = "AC", width = 5, height = 2, activebackground= 'red', command = lambda: borrar())
boton_back = Button(ventana, text =chr(9003), width = 5, height = 2, activebackground= 'magenta', command = lambda: back())
boton_parentesis1 = Button(ventana, text = "(", width = 5, height = 2, activebackground= 'beige', command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, activebackground= 'blueviolet', command = lambda: click_boton(")"))
boton_punto = Button(ventana, text = ".", width = 5, height = 2, activebackground= 'burlywood', command = lambda: click_boton("."))
boton_ON =Button(ventana, text = "ON", width = 5, height = 2, activebackground= 'chartreuse', command = lambda: Cambio())

boton_div = Button(ventana, text = "/", width = 5, height = 2,activebackground= 'darkgreen', command = lambda: click_boton("/"))
boton_mult = Button(ventana, text = "x", width = 5, height = 2,activebackground= 'orangered', command = lambda: click_boton("*"))
boton_sum = Button(ventana, text = "+", width = 5, height = 2,activebackground= 'gold', command = lambda: click_boton("+"))
boton_rest = Button(ventana, text = "-", width = 5, height = 2,activebackground= 'olive', command = lambda: click_boton("-"))
boton_igual = Button(ventana, text = "=", width = 5, height = 2,activebackground= 'wheat', command = lambda: hacer_operacion())

# Boton j para unidad imaginaria
boton_j = Button(ventana, text = "j", width = 5, height = 2,activebackground= 'red', command = lambda: click_boton("j"))

#agregar  botones en pantalla
boton_borrar.grid(row = 1, column= 5, padx= 5, pady = 5)
boton_back.grid(row = 1, column= 0, padx= 5, pady = 5)
boton_parentesis1.grid(row = 1, column= 1, padx= 5, pady = 5)
boton_parentesis2.grid(row = 1, column= 2, padx= 5, pady = 5)
boton_div.grid(row = 1, column= 3, padx= 5, pady = 5)

boton7.grid(row = 2, column= 0, padx= 5, pady = 5)
boton8.grid(row = 2, column= 1, padx= 5, pady = 5)
boton9.grid(row = 2, column= 2, padx= 5, pady = 5)
boton_mult.grid(row = 2, column= 3, padx= 5, pady = 5)


boton4.grid(row = 3, column= 0, padx= 5, pady = 5)
boton5.grid(row = 3, column= 1, padx= 5, pady = 5)
boton6.grid(row = 3, column= 2, padx= 5, pady = 5)
boton_sum.grid(row = 3, column= 3, padx= 5, pady = 5)

boton1.grid(row = 4, column= 0, padx= 5, pady = 5)
boton2.grid(row = 4, column= 1, padx= 5, pady = 5)
boton3.grid(row = 4, column= 2, padx= 5, pady = 5)
boton_rest.grid(row = 4, column= 3, padx= 5, pady = 5)

boton0.grid(row = 5, column= 0,columnspan = 2, padx= 5, pady = 5)
boton_punto.grid(row = 5, column= 2, padx= 5, pady = 5)
boton_igual.grid(row = 5, column= 3, padx= 5, pady = 5)
boton_j.grid(row = 4, column= 5, padx= 5, pady = 5)
boton_ON.grid(row = 5, column= 5, padx= 5, pady = 5)

ventana.mainloop()