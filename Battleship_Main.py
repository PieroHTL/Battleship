import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)

        # Erstelle das Layout und füge die Knöpfe hinzu
        layout = QGridLayout()
        
        # Erstelle die Knöpfe mit einer Schleife
        self.buttons = []
        for x in range(10):
            for y in range(10):
                button = QPushButton()
                self.buttons.append(button)
                layout.addWidget(button, x,y)
        
        
        # Setze das Layout als Layout des Widgets
        self.setLayout(layout)
        #Fesnter benennen
        self.setWindowTitle("Battleship")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
