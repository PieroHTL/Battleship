import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtNetwork import QTcpServer, QTcpSocket
from PyQt6.QtCore import QByteArray, QDataStream, QIODevice

class MyServer(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,200)

        self.tcpServer =QTcpServer()
        self.tcpServer.newConnection.connect(self.on_new_connection)
        self.tcpServer.listen(port =6002)

    def on_new_connection(self):
        clientConnection =self.tcpServer.nextPendingConnection()
        clientConnection.readyRead.connect(self.on_ready_read)
        clientConnection.disconnected.connect(self.on_disconnected)

    def on_ready_read(self):
        clientConnection =self.sender()

        data =clientConnection.readAll()
        stream =QDataStream(data, QIODevice.ReadOnly)
        message_type =stream.readInt32()
        message =stream.readQString()

        if(message_type ==1):
            print(f"Button clicked: {message}")

    def on_disconnected(self):
        clientConnection =self.sender()
        clientConnection.deleteLater()

if(__name__ == "__main__"):
    app =QApplication(sys.argv)
    server =MyServer()
    sys.exit(app.exec())