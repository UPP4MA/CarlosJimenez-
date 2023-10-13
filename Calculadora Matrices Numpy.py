import tkinter as tk
from tkinter import ttk
import numpy as np

class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrices")

        self.create_widgets()

    def create_widgets(self):
        # Matrices de entrada
        self.matrix_a_label = ttk.Label(self.root, text="Matriz A:")
        self.matrix_b_label = ttk.Label(self.root, text="Matriz B:")

        self.matrix_a_entry = ttk.Entry(self.root, width=20)
        self.matrix_b_entry = ttk.Entry(self.root, width=20)

        # Botones de operaciones
        add_button = ttk.Button(self.root, text="Sumar", command=self.add_matrices)
        subtract_button = ttk.Button(self.root, text="Restar", command=self.subtract_matrices)
        multiply_button = ttk.Button(self.root, text="Multiplicar", command=self.multiply_matrices)

        # Resultado
        self.result_label = ttk.Label(self.root, text="Resultado:")
        self.result_entry = ttk.Entry(self.root, width=20, state="readonly")

        # Posicionamiento de los elementos en la interfaz
        self.matrix_a_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.matrix_a_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.matrix_b_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.matrix_b_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        add_button.grid(row=2, column=0, padx=5, pady=5)
        subtract_button.grid(row=2, column=1, padx=5, pady=5)
        multiply_button.grid(row=2, column=2, padx=5, pady=5)
        self.result_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.result_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    def add_matrices(self):
        matrix_a = self.get_matrix_from_entry(self.matrix_a_entry)
        matrix_b = self.get_matrix_from_entry(self.matrix_b_entry)

        if matrix_a is not None and matrix_b is not None:
            result = np.add(matrix_a, matrix_b)
            self.display_result(result)

    def subtract_matrices(self):
        matrix_a = self.get_matrix_from_entry(self.matrix_a_entry)
        matrix_b = self.get_matrix_from_entry(self.matrix_b_entry)

        if matrix_a is not None and matrix_b is not None:
            result = np.subtract(matrix_a, matrix_b)
            self.display_result(result)

    def multiply_matrices(self):
        matrix_a = self.get_matrix_from_entry(self.matrix_a_entry)
        matrix_b = self.get_matrix_from_entry(self.matrix_b_entry)

        if matrix_a is not None and matrix_b is not None:
            result = np.dot(matrix_a, matrix_b)
            self.display_result(result)

    def get_matrix_from_entry(self, entry):
        try:
            matrix_text = entry.get()
            matrix = np.array(eval(matrix_text))
            return matrix
        except Exception as e:
            print(f"Error al obtener la matriz: {e}")
            return None

    def display_result(self, result):
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(result))
        self.result_entry.config(state="readonly")

# Crear la aplicación
root = tk.Tk()
app = MatrixCalculatorApp(root)
root.mainloop()
