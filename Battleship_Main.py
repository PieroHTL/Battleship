import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtNetwork import QTcpSocket
from PyQt6.QtCore import QByteArray, QDataStream, QIODevice

# Importiere benötigte Bibliotheken

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,200)
        # Definiere Größe des Fensters

        self.button1 = QPushButton("Button 1")
        self.button1.clicked.connect(self.onButton1Clicked)

        self.button2 = QPushButton("Button 2")
        self.button2.clicked.connect(self.onButton2Clicked)

        self.button3 = QPushButton("Button 3")
        self.button3.clicked.connect(self.onButton3Clicked)

        self.button4 = QPushButton("Button 4")
        self.button4.clicked.connect(self.onButton4Clicked)
        # Definiere 4 Buttons und verbinde sie mit ihren zugehörigen Funktionen

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        # Definiere ein vertikales Layout und füge alle Buttons hinzu

        self.setLayout(layout)
        # Setze das Layout als das Layout für das Widget

    def onButton1Clicked(self):
        print("Button 1 clicked")
        # Funktion, die aufgerufen wird, wenn Button 1 geklickt wird und eine Ausgabe auf der Konsole ausgibt

    def onButton2Clicked(self):
        print("Button 2 clicked")
        # Funktion, die aufgerufen wird, wenn Button 2 geklickt wird und eine Ausgabe auf der Konsole ausgibt

    def onButton3Clicked(self):
        print("Button 3 clicked")
        # Funktion, die aufgerufen wird, wenn Button 3 geklickt wird und eine Ausgabe auf der Konsole ausgibt

    def onButton4Clicked(self):
        print("Button 4 clicked")
        # Funktion, die aufgerufen wird, wenn Button 4 geklickt wird und eine Ausgabe auf der Konsole ausgibt

    def on_button_clicked(self):
        # Funktion, die aufgerufen wird, wenn ein Button geklickt wird

        socket = QTcpSocket()
        # Erstelle ein QTcpSocket-Objekt

        socket.connectToHost("localhost", 1234)
        # Stelle eine Verbindung zu einem Host mit der IP-Adresse "localhost" und dem Port 1234 her

        data = QByteArray()
        # Erstelle ein QByteArray-Objekt

        stream = QDataStream(data, QIODevice.WriteOnly)
        # Erstelle ein QDataStream-Objekt, um Daten in das QByteArray-Objekt zu schreiben

        stream.writeInt32(1)
        # Schreibe eine 32-Bit-Ganzzahl in das QDataStream-Objekt

        stream.writeQString("Button Clicked")
        # Schreibe eine Zeichenkette in das QDataStream-Objekt

        socket.write(data)
        # Schreibe die Daten aus dem QByteArray-Objekt in den Socket

        socket.flush()
        # Sende die Daten aus dem Socket an den Host

        socket.disconnectFromHost()
        # Trenne die Verbindung zum Host

        socket.waitForDisconnected()
        # Warte, bis die Verbindung zum Host getrennt ist

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())