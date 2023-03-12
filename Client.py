import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QTcpSocket
from PyQt6.QtCore import QByteArray, QDataStream, QIODevice

def Client():
    socket = QTcpSocket()
    socket.connectToHost("localhost", 6002)

    data = QByteArray()
    stream = QDataStream(data, QIODevice.WriteOnly)
    #stream.writeInt32(1)
    #stream.writeQString()

    socket.write(data)
    socket.flush()
    socket.disconnectFromHost()
    socket.waitForDisconnected()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #widget = ()
    #widget.show()
    sys.exit(app.exec())