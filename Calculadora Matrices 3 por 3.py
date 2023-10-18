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
        self.matrix_a_label = ttk.Label(self.root, text="Matriz A :")
        self.matrix_b_label = ttk.Label(self.root, text="Matriz B :")

        self.matrix_a_entries = [[ttk.Entry(self.root, width=5) for _ in range(3)] for _ in range(3)]
        self.matrix_b_entries = [[ttk.Entry(self.root, width=5) for _ in range(3)] for _ in range(3)]

        # Botones de operaciones
        add_button = ttk.Button(self.root, text="Sumar", command=self.add_matrices)
        subtract_button = ttk.Button(self.root, text="Restar", command=self.subtract_matrices)
        multiply_button = ttk.Button(self.root, text="Multiplicar", command=self.multiply_matrices)
        inverse_button = ttk.Button(self.root, text="Inversa", command=self.calculate_inverse)

        # Resultado
        self.result_label = ttk.Label(self.root, text="Resultado:")
        self.result_entry = ttk.Entry(self.root, width=20, state="readonly")

        # Posicionamiento de los elementos en la interfaz
        self.matrix_a_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.matrix_b_label.grid(row=0, column=4, padx=5, pady=5, sticky="e")

        for i in range(3):
            for j in range(3):
                self.matrix_a_entries[i][j].grid(row=i, column=j+1, padx=5, pady=5)
                self.matrix_b_entries[i][j].grid(row=i, column=j+5, padx=5, pady=5)

        add_button.grid(row=4, column=1, padx=5, pady=5)
        subtract_button.grid(row=4, column=2, padx=5, pady=5)
        multiply_button.grid(row=4, column=3, padx=5, pady=5)
        inverse_button.grid(row=4, column=4, padx=5, pady=5)
        self.result_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.result_entry.grid(row=5, column=1, columnspan=4, padx=5, pady=5, sticky="w")

    def get_matrices_from_entries(self, entries):
        try:
            matrix = [[float(entry.get()) for entry in row] for row in entries]
            return np.array(matrix)
        except ValueError:
            print("Error al obtener la matriz. Asegúrate de ingresar números válidos.")
            return None

    def add_matrices(self):
        matrix_a = self.get_matrices_from_entries(self.matrix_a_entries)
        matrix_b = self.get_matrices_from_entries(self.matrix_b_entries)

        if matrix_a is not None and matrix_b is not None:
            result = np.add(matrix_a, matrix_b)
            self.display_result(result)

    def subtract_matrices(self):
        matrix_a = self.get_matrices_from_entries(self.matrix_a_entries)
        matrix_b = self.get_matrices_from_entries(self.matrix_b_entries)

        if matrix_a is not None and matrix_b is not None:
            result = np.subtract(matrix_a, matrix_b)
            self.display_result(result)

    def multiply_matrices(self):
        matrix_a = self.get_matrices_from_entries(self.matrix_a_entries)
        matrix_b = self.get_matrices_from_entries(self.matrix_b_entries)

        if matrix_a is not None and matrix_b is not None:
            result = np.dot(matrix_a, matrix_b)
            self.display_result(result)

    def calculate_inverse(self):
        matrix_a = self.get_matrices_from_entries(self.matrix_a_entries)

        if matrix_a is not None:
            try:
                inverse_matrix = np.linalg.inv(matrix_a)
                self.display_result(inverse_matrix)
            except np.linalg.LinAlgError:
                self.display_result("No se puede calcular la inversa. Asegúrate de que la matriz sea invertible.")

    def display_result(self, result):
        formatted_result = "\n".join(["\t".join(map(str, row)) for row in result])
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(result))
        self.result_entry.config(state="readonly")
    
# Crear la aplicación
root = tk.Tk()
app = MatrixCalculatorApp(root)
root.mainloop()