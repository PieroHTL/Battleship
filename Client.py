import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QTcpSocket
from PyQt6.QtCore import QByteArray, QDataStream, QIODevice

def client():
    socket = QTcpSocket() #Creates a QTcpSocket instance over TCP/IP
    socket.connectToHost("localhost", 6002) #Establishes a connection to host

    data = QByteArray() #Variable will be used to store data
    stream = QDataStream(data, QIODevice.WriteOnly) #Attaches a data stream to the data variable for writing data
    stream.writeInt32(1) #Writes an integer to the data stream
    stream.writeQString("Something has been done :)")

    socket.write(data)
    socket.flush() #Waits until all data in the socket's buffer has been written
    socket.disconnectFromHost()
    socket.waitForDisconnected()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #widget = ()
    #widget.show()
    sys.exit(app.exec())