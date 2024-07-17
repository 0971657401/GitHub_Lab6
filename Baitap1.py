# Họ và tên: Phan Nguyễn Thế Vinh
# MSSV: 2100011204

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bài tập 1")
        self.setGeometry(100, 100, 600, 300)  # Đặt kích thước cửa sổ chính

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f8ff;
            }
            QWidget {
                background-color: #B5B5B5;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 20px;
            }
            QLabel {
                font-size: 24px;
                color: white;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 20px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                width: 80px;
                text-align: center;
            }
            QPushButton {
                font-size: 20px;
                padding: 10px;
                border-radius: 5px;
                background-color: white;
                color: black;
                width: 100px;
            }
            QPushButton:hover {
                background-color: #CC99FF;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)

        self.titleLabel = QLabel("Frame Recorder")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.inputLabel = QLabel("Create an")
        self.inputField = QLineEdit()
        self.inputField.setText("100")  # Default value
        self.inputSuffix = QLabel("FPS video")

        inputLayout = QHBoxLayout()
        inputLayout.addStretch()
        inputLayout.addWidget(self.inputLabel, alignment=Qt.AlignCenter)
        inputLayout.addWidget(self.inputField, alignment=Qt.AlignCenter)
        inputLayout.addWidget(self.inputSuffix, alignment=Qt.AlignCenter)
        inputLayout.addStretch()

        self.pauseButton = QPushButton("Pause")
        self.startButton = QPushButton("Start")
        self.endButton = QPushButton("End")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.pauseButton, alignment=Qt.AlignCenter)
        buttonLayout.addWidget(self.startButton, alignment=Qt.AlignCenter)
        buttonLayout.addWidget(self.endButton, alignment=Qt.AlignCenter)
        buttonLayout.addStretch()

        self.statusLabel = QLabel("Recording Paused")
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setStyleSheet("font-size: 18px; color: #333;")

        layout = QVBoxLayout()
        layout.addWidget(self.titleLabel)
        layout.addLayout(inputLayout)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.statusLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
