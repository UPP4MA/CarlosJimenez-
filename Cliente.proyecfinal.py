import tkinter as tk
from tkinter import ttk, messagebox
import socket

class ArduinoGUI:
    def __init__(self, root):
        # ... (your existing code)

        # New variable for client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # ... (your existing code)

    def connect_to_server(self):
        # Connect to the server
        try:
            self.client_socket.connect(('localhost', 5555))  # You can change the IP and port accordingly
            messagebox.showinfo("Connection Successful", "Connected to the server successfully.")
        except socket.error as e:
            messagebox.showerror("Connection Error", f"Failed to connect to the server: {e}")

    def update_speed(self, value):
        # Update the speed in the client and send it to the server
        try:
            speed = int(value)
            self.client_socket.sendall(str(speed).encode())
        except (ValueError, socket.error):
            pass

# ... (the rest of your code)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoGUI(root)
    app.connect_to_server()  # Connect to the server when the GUI starts
    root.mainloop()
