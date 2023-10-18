import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button

def resolver_sistema():
    # Obtener los coeficientes de las ecuaciones desde las cajas de entrada
    a11 = float(entry_a11.get())
    a12 = float(entry_a12.get())
    a13 = float(entry_a13.get())
    b1 = float(entry_b1.get())

    a21 = float(entry_a21.get())
    a22 = float(entry_a22.get())
    a23 = float(entry_a23.get())
    b2 = float(entry_b2.get())

    a31 = float(entry_a31.get())
    a32 = float(entry_a32.get())
    a33 = float(entry_a33.get())
    b3 = float(entry_b3.get())

    # Coeficientes de las ecuaciones en forma de matriz
    A = np.array([[a11, a12, a13],
                  [a21, a22, a23],
                  [a31, a32, a33]])

    # Lado derecho de las ecuaciones en forma de vector
    b = np.array([b1, b2, b3])

    # Resolver el sistema de ecuaciones
    x = np.linalg.solve(A, b)

    # Mostrar la solución en la etiqueta de resultado
    resultado.set(f"La solución es: x = {x[0]}, y = {x[1]}, z = {x[2]}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Solver de Sistema de Ecuaciones")

# Crear cajas de entrada y etiquetas para los coeficientes
entry_a11 = Entry(ventana)
entry_a12 = Entry(ventana)
entry_a13 = Entry(ventana)
entry_b1 = Entry(ventana)

entry_a21 = Entry(ventana)
entry_a22 = Entry(ventana)
entry_a23 = Entry(ventana)
entry_b2 = Entry(ventana)

entry_a31 = Entry(ventana)
entry_a32 = Entry(ventana)
entry_a33 = Entry(ventana)
entry_b3 = Entry(ventana)

# Etiquetas para los coeficientes
Label(ventana, text="Coeficientes x:").grid(row=0, column=0, sticky='w')
Label(ventana, text="Coeficientes y:").grid(row=1, column=0, sticky='w')
Label(ventana, text="Coeficientes z:").grid(row=2, column=0, sticky='w')

# Ubicar las cajas de entrada
entry_a11.grid(row=0, column=1)
entry_a12.grid(row=0, column=2)
entry_a13.grid(row=0, column=3)
entry_b1.grid(row=0, column=4)

entry_a21.grid(row=1, column=1)
entry_a22.grid(row=1, column=2)
entry_a23.grid(row=1, column=3)
entry_b2.grid(row=1, column=4)

entry_a31.grid(row=2, column=1)
entry_a32.grid(row=2, column=2)
entry_a33.grid(row=2, column=3)
entry_b3.grid(row=2, column=4)

# Botón para resolver el sistema
Button(ventana, text="Resolver", command=resolver_sistema).grid(row=3, column=0, columnspan=5)

# Etiqueta para mostrar el resultado
resultado = tk.StringVar()
Label(ventana, textvariable=resultado).grid(row=4, column=0, columnspan=5)

# Iniciar el bucle de eventos
ventana.mainloop()
