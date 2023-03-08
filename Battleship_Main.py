import sys
from PyQt6.QtWidgets import QApplication, QWidget

# Create the application instance
app = QApplication(sys.argv)

# Create a window
window = QWidget()
window.setWindowTitle('Empty Main Window')

# Show the window
window.show()

# Start the event loop
sys.exit(app.exec())
