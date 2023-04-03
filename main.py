import sys
import resource_rc
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent, QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(":/icon.ico"))
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        initial_width, initial_height = 960, 120
        window_width, window_height = 1920, 1080
        self.setGeometry((window_width - initial_width) // 2, window_height - 2 * initial_height,
                         initial_width, initial_height)
        self.setMinimumSize(20, 20)
        self.setStyleSheet("background-color: white;")
        self.offset = None
        self.setWindowOpacity(1.0)  # set initial opacity to 100%

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent):
        # change opacity with mouse wheel
        opacity = self.windowOpacity()
        if event.angleDelta().y() > 0:
            opacity += 0.05
        else:
            opacity -= 0.05
        opacity = max(0.1, min(opacity, 1.0))  # limit opacity to 10-100%
        self.setWindowOpacity(opacity)
        event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Space:
            if self.windowOpacity() > 0.5:
                self.setWindowOpacity(0.1)
            else:
                self.setWindowOpacity(1.0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
