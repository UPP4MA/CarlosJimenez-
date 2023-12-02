import socket
import threading

class ArduinoServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 5555))  # You can change the IP and port accordingly
        self.server_socket.listen(1)
        print("Server listening on port 5555")

        self.connection, self.client_address = self.server_socket.accept()
        print("Client connected:", self.client_address)

    def start_server(self):
        threading.Thread(target=self.receive_data).start()

    def receive_data(self):
        while True:
            try:
                data = self.connection.recv(1024).decode()
                if not data:
                    break
                print("Received data from client:", data)

                # Execute the received data (assuming it's a speed value)
                speed = int(data)
                # Implement your code to control the motors using the received speed value

            except socket.error as e:
                print("Error receiving data:", e)
                break

    def close_server(self):
        self.server_socket.close()

if __name__ == "__main__":
    server = ArduinoServer()
    server.start_server()
