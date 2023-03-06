from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
import time

class Worker(QObject):
    data_updated = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self._stop = False

    def stop(self):
        self._stop = True

    def run(self):
        i = 0
        while not self._stop:
            data = f"Data {i}"
            self.data_updated.emit(data)
            i += 1
            time.sleep(1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("Waiting for data...")
        self.start_button = QPushButton("Start processing")
        self.stop_button = QPushButton("Stop processing")
        self.stop_button.setEnabled(False)

        self.start_button.clicked.connect(self.start_processing)
        self.stop_button.clicked.connect(self.stop_processing)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.worker = None

    def start_processing(self):
        self.label.setText("Processing...")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        self.worker = Worker()
        self.worker.data_updated.connect(self.update_data)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def stop_processing(self):
        self.worker.stop()
        self.thread.quit()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_data(self, data):
        self.label.setText(data)

    def closeEvent(self, event):
        if self.worker:
            self.worker.stop()
            self.thread.quit()
            self.thread.wait()

        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
