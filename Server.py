import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtNetwork import QTcpServer, QTcpSocket
from PyQt6.QtCore import QByteArray, QDataStream, QIODevice

class MyServer(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,200)

        self.tcpServer =QTcpServer()
        self.tcpServer.newConnection.connect(self.on_new_connection) #Creates a QTcpServer instance and sets up a signal-slot connection to handle new client connections
        self.tcpServer.listen(port =6002)

    def on_new_connection(self):
        clientConnection =self.tcpServer.nextPendingConnection() #Gets the next pending client connection and sets it up to signal-slot connections to handle incoming data and disconnections
        clientConnection.readyRead.connect(self.on_ready_read)
        clientConnection.disconnected.connect(self.on_disconnected)

    def on_ready_read(self):
        clientConnection =self.sender() #Grabs the client connection

        data =clientConnection.readAll()
        stream =QDataStream(data, QIODevice.ReadOnly) #Pass down the data and only restrict to only read
        message_type =stream.readInt32() #Analyse the message type
        message =stream.readQString() #read

        if(message_type ==1):
            print(f"Button clicked: {message}")

    def on_disconnected(self):
        clientConnection =self.sender() #Gets the client info, returns a pointer to the object that sent the signal
        clientConnection.deleteLater() #Deleted the connect client

if(__name__ == "__main__"):
    app =QApplication(sys.argv)
    server =MyServer()
    sys.exit(app.exec())