import sys, socket, threading
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit,QHBoxLayout, QMainWindow, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        # Creating a grid layout
        layout = QGridLayout()

        # Adding labels
        self.username_label = QLabel("Username")
        self.password_label = QLabel("Password")

        # Adding input fields
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Adding placeholder text
        self.username_input.setPlaceholderText("Enter your username")
        self.password_input.setPlaceholderText("Enter your password")

        # Adding submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)

        # Adding the labels and input fields to the grid layout
        layout.addWidget(self.username_label, 0, 0)
        layout.addWidget(self.password_label, 1, 0)
        layout.addWidget(self.username_input, 0, 1)
        layout.addWidget(self.password_input, 1, 1)
        layout.addWidget(self.submit_button, 2, 1)

        self.setLayout(layout)

    def submit(self):
        # Get the data from the input fields
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if the entered data is valid
        if not username:
            #ERROR message box if text is invalid
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Icon.Warning)
            error_message.setWindowTitle("ERROR")
            error_message.setText("Please enter a username.")
            error_message.exec()
            return

        elif not password:
            #ERROR message box if text is invalid
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Icon.Warning)
            error_message.setWindowTitle("ERROR")
            error_message.setText("Please enter a password.")
            error_message.exec()
            return

        elif username != "admin" or password != "admin":
            #ERROR message box if text is invalid
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Icon.Warning)
            error_message.setWindowTitle("ERROR")
            error_message.setText("Invalid username or password.")
            error_message.exec()
            return
            
        # Login message box
        login_message = QMessageBox()
        login_message.setIcon(QMessageBox.Icon.Information)
        login_message.setWindowTitle("Login successful")
        login_message.setText("Login was successful!")
        login_message.exec()

        # Close the window
        self.close()

        # opens after login page is closed
        self.new_window =ButtonField()
        self.new_window.show()

class ButtonField(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        layout =QGridLayout()

        #Create buttons with a loop
        self.buttons =[]
        for x in range(10):
            for y in range(10):
                button =QPushButton()
                button.clicked.connect(lambda _, x=x, y=y: self.send_shot(x, y)) #Connect the clicked signal of each button to the send_shot method with the coordinates of the button as arguments
                self.buttons.append(button)
                layout.addWidget(button, x, y)

        self.setLayout(layout) #Set the layout as the widget layout 
        self.setWindowTitle("Battleship")

        self.socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #add_in =input("Enter add >")
        #port_in =input("Enter port >")
        self.socket.connect(('localhost', 6002))

        threading.Thread(target=self.receive_data).start() #Starts a thread that receives data from the server

    def receive_data(self):
        while True:
            data =self.socket.recv(1024)
            if not data:
                break

    def send_shot(self, x, y):
        self.socket.send(f'{x},{y}'.encode()) #The coordinates of the clicked buttons are being send to the server as a string

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =LoginWindow()
    window.show()
    sys.exit(app.exec())