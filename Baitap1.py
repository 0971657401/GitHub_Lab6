# Họ và tên: Phan Nguyễn Thế Vinh
#MSSV: 2100011204

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QWidget, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bài tập 1")
        self.setGeometry(100, 100, 600, 300)  # Đặt kích thước cửa sổ chính

        # Đặt kiểu giao diện bằng CSS
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
                border-radius: 10px;
                background-color: #4CAF50;
                color: white;
                width: 100px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #397d3f;
            }
        """)

        # Tạo nhãn tiêu đề
        self.titleLabel = QLabel("Frame Recorder")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # Tạo các nhãn và ô nhập liệu
        self.inputLabel = QLabel("Create an")
        self.inputField = QLineEdit()
        self.inputField.setText("100")  # Giá trị mặc định
        self.inputSuffix = QLabel("FPS video")

        # Bố trí cho phần nhập liệu
        inputLayout = QHBoxLayout()
        inputLayout.addStretch()
        inputLayout.addWidget(self.inputLabel, alignment=Qt.AlignCenter)
        inputLayout.addWidget(self.inputField, alignment=Qt.AlignCenter)
        inputLayout.addWidget(self.inputSuffix, alignment=Qt.AlignCenter)
        inputLayout.addStretch()

        # Tạo các nút bấm và kết nối với các phương thức hiển thị thông báo
        self.pauseButton = QPushButton("Pause")
        self.pauseButton.clicked.connect(self.show_pause_message)

        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.show_start_message)

        self.endButton = QPushButton("End")
        self.endButton.clicked.connect(self.show_end_message)

        # Bố trí cho các nút bấm
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.pauseButton, alignment=Qt.AlignCenter)
        buttonLayout.addWidget(self.startButton, alignment=Qt.AlignCenter)
        buttonLayout.addWidget(self.endButton, alignment=Qt.AlignCenter)
        buttonLayout.addStretch()

        # Tạo nhãn trạng thái
        self.statusLabel = QLabel("Recording Paused")
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setStyleSheet("font-size: 18px; color: #333;")

        # Bố trí chính của giao diện
        layout = QVBoxLayout()
        layout.addWidget(self.titleLabel)
        layout.addLayout(inputLayout)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.statusLabel)

        # Thiết lập container và giao diện chính
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Phương thức hiển thị thông báo khi nhấn nút Pause
    def show_pause_message(self):
        QMessageBox.information(self, "Pause", "OK Pause")

    # Phương thức hiển thị thông báo khi nhấn nút Start
    def show_start_message(self):
        QMessageBox.information(self, "Start", "OK Started")

    # Phương thức hiển thị thông báo khi nhấn nút End
    def show_end_message(self):
        QMessageBox.information(self, "End", "OK Ended")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
