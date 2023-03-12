import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import socket
import threading

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        layout = QGridLayout()

        self.buttons = []
        for x in range(10):
            for y in range(10):
                button = QPushButton()
                button.clicked.connect(lambda _, x=x, y=y: self.send_shot(x, y))
                self.buttons.append(button)
                layout.addWidget(button, x, y)

        self.setLayout(layout)
        self.setWindowTitle("Battleship")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #add_in =input("Enter add >")
        #port_in =input("Enter port >")
        self.socket.connect(('localhost', 6002))

        threading.Thread(target=self.receive_data).start()

    def receive_data(self):
        while True:
            data = self.socket.recv(1024)
            if not data:
                break

    def send_shot(self, x, y):
        self.socket.send(f'{x},{y}'.encode())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())