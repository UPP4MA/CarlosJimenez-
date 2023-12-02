import tkinter as tk
from tkinter import ttk, messagebox
import serial
import time

class ArduinoGUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Control de Arduino")

        # Variables
        self.arduino_port = tk.StringVar()
        self.distance_label_var = tk.StringVar()
        self.speed_var = tk.DoubleVar()
        self.speed_var.set(0)  # Valor predeterminado para la velocidad

        # Crear elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y cuadro de entrada para el puerto de Arduino
        port_label = ttk.Label(self.root, text="Puerto de Arduino:")
        port_entry = ttk.Entry(self.root, textvariable=self.arduino_port)
        port_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        port_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Botón para conectar a Arduino
        connect_button = ttk.Button(self.root, text="Conectar", command=self.connect_to_arduino)
        connect_button.grid(row=0, column=2, padx=10, pady=10)

        # Etiqueta para mostrar la distancia del sensor ultrasónico
        distance_label = ttk.Label(self.root, text="Distancia del sensor:")
        distance_value_label = ttk.Label(self.root, textvariable=self.distance_label_var)
        distance_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        distance_value_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="w")

        # Barra de velocidad para controlar la velocidad de los motores
        speed_label = ttk.Label(self.root, text="Velocidad de los motores:")
        speed_scale = ttk.Scale(self.root, from_=0, to=255, variable=self.speed_var, orient="horizontal", command=self.update_speed)
        speed_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        speed_scale.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")

    def update_speed(self, value):
        # Actualizar la velocidad en el Arduino cuando la barra se ajusta
        try:
            speed = int(value)
            self.ser.write(f'{speed}\n'.encode())
        except (ValueError, serial.SerialException):
            pass

    def connect_to_arduino(self):
        # Conectar a Arduino utilizando el puerto especificado
        port = self.arduino_port.get()
        try:
            self.ser = serial.Serial(port, 9600, timeout=1)
            time.sleep(2)  # Esperar a que Arduino se reinicie después de la conexión
            self.update_distance()
            messagebox.showinfo("Conexión Exitosa", "Conexión establecida correctamente con Arduino.")
        except serial.SerialException as e:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar a Arduino: {e}")

    def update_distance(self):
        # Leer datos del sensor ultrasónico y actualizar la etiqueta
        try:
            self.ser.write(b'M')  # Enviar comando para medir distancia desde Arduino
            distance_str = self.ser.readline().decode().strip()
            self.distance_label_var.set(distance_str + " cm")

            # Añadido: Enviar la velocidad a Arduino
            speed = int(self.speed_var.get())
            self.ser.write(f'S{speed}\n'.encode())

            self.root.after(100, self.update_distance)  # Actualizar cada 100 ms
        except (serial.SerialException, UnicodeDecodeError):
            messagebox.showerror("Error de Lectura", "Error al leer desde Arduino")

if __name__ == "_main_":
    root = tk.Tk()
    app = ArduinoGUI(root)
    root.mainloop()