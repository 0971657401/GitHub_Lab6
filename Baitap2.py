# Họ và tên: Phan Nguyễn Thế Vinh
#MSSV: 2100011204

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bài tập 2")
        self.setGeometry(100, 100, 900, 600)  # Đặt kích thước cửa sổ chính

        # Đặt kiểu giao diện bằng CSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QWidget {
                background-color: #104E8B;
            }
            QLabel {
                font-size: 24px;
                color: white;
                font-weight: bold;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                background-color: magenta;
                color: white;
                border: 2px solid white;
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                border: 2px solid black;
                background-color: black;
            }
            QPushButton:pressed {
                background-color: #cc00cc;
            }
        """)

        # Tạo sidebar (bên trái)
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #C0C0C0; color: white;")

        # Tạo nhãn tiêu đề cho sidebar
        self.statusLabel = QLabel("AtarBals AntiVirus")
        self.statusLabel.setAlignment(Qt.AlignLeft)
        self.statusLabel.setStyleSheet("font-size: 20px; padding: 20px; font-weight: bold; color: black;")

        # Tạo các nút trong sidebar và kết nối với các phương thức hiển thị thông báo
        self.statusButton = QPushButton("Status")
        self.statusButton.setStyleSheet("""
            background-color: #1E90FF; color: white;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.statusButton.clicked.connect(lambda: self.show_message("Status"))

        self.updateButton = QPushButton("Updates")
        self.updateButton.setStyleSheet("""
            background-color: #32CD32; color: white;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.updateButton.clicked.connect(lambda: self.show_message("Updates"))

        self.settingsButton = QPushButton("Settings")
        self.settingsButton.setStyleSheet("""
            background-color: #FF8C00; color: white;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.settingsButton.clicked.connect(lambda: self.show_message("Settings"))

        self.feedbackButton = QPushButton("Share Feedback")
        self.feedbackButton.setStyleSheet("""
            background-color: #DA70D6; color: white;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.feedbackButton.clicked.connect(lambda: self.show_message("Share Feedback"))

        self.premiumButton = QPushButton("Buy Premium")
        self.premiumButton.setStyleSheet("""
            background-color: #8B0000; color: white;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.premiumButton.clicked.connect(lambda: self.show_message("Buy Premium"))

        self.helpButton = QPushButton("Help")
        self.helpButton.setStyleSheet("""
            background-color: #4B0082; color: white;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.helpButton.clicked.connect(lambda: self.show_message("Help"))

        self.scanNowButton = QPushButton("Scan Now")
        self.scanNowButton.setStyleSheet("""
            background-color: #00FF00; color: black; border: 2px solid black;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.scanNowButton.clicked.connect(lambda: self.show_message("Scan Now"))

        # Bố trí các nút trong sidebar
        sidebarLayout = QVBoxLayout()
        sidebarLayout.addWidget(self.statusLabel)
        sidebarLayout.addWidget(self.statusButton)
        sidebarLayout.addWidget(self.updateButton)
        sidebarLayout.addWidget(self.settingsButton)
        sidebarLayout.addWidget(self.feedbackButton)
        sidebarLayout.addWidget(self.premiumButton)
        sidebarLayout.addWidget(self.helpButton)
        sidebarLayout.addStretch()
        sidebarLayout.addWidget(self.scanNowButton)
        self.sidebar.setLayout(sidebarLayout)

        # Bố trí chính cho phần nội dung
        self.titleLabel = QLabel("Scan")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.subtitleLabel = QLabel("Premium will be free forever. You just need to click button.")
        self.subtitleLabel.setAlignment(Qt.AlignCenter)
        self.subtitleLabel.setStyleSheet("font-size: 16px; color: white;")

        self.quickScanButton = QPushButton("Quick Scan")
        self.quickScanButton.setStyleSheet("""
            background-color: white; color: black; border: 2px solid black;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.quickScanButton.clicked.connect(lambda: self.show_message("Quick Scan"))

        self.webProtectionButton = QPushButton("Web Protection")
        self.webProtectionButton.setStyleSheet("""
            background-color: white; color: black; border: 2px solid black;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.webProtectionButton.clicked.connect(lambda: self.show_message("Web Protection"))

        self.quarantineButton = QPushButton("Quarantine")
        self.quarantineButton.setStyleSheet("""
            background-color: white; color: black; border: 2px solid black;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.quarantineButton.clicked.connect(lambda: self.show_message("Quarantine"))

        self.fullScanButton = QPushButton("Full Scan")
        self.fullScanButton.setStyleSheet("""
            background-color: white; color: black; border: 2px solid black;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.fullScanButton.clicked.connect(lambda: self.show_message("Full Scan"))

        self.simpleUpdateButton = QPushButton("Simple Update")
        self.simpleUpdateButton.setStyleSheet("""
            background-color: white; color: black; border: 2px solid black;
            QPushButton:hover {
                border: 2px solid yellow;
            }
        """)
        self.simpleUpdateButton.clicked.connect(lambda: self.show_message("Simple Update"))

        # Bố trí các nút chính
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.quickScanButton)
        buttonLayout.addWidget(self.webProtectionButton)
        buttonLayout.addWidget(self.quarantineButton)
        buttonLayout.addWidget(self.fullScanButton)
        buttonLayout.addWidget(self.simpleUpdateButton)

        self.premiumLabel = QLabel("Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}")
        self.premiumLabel.setAlignment(Qt.AlignCenter)
        self.premiumLabel.setStyleSheet("font-size: 14px; color: magenta;")

        mainContentLayout = QVBoxLayout()
        mainContentLayout.addWidget(self.titleLabel)
        mainContentLayout.addWidget(self.subtitleLabel)
        mainContentLayout.addLayout(buttonLayout)
        mainContentLayout.addWidget(self.premiumLabel)

        mainContent = QWidget()
        mainContent.setLayout(mainContentLayout)

        # Bố trí tổng thể
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.sidebar)
        mainLayout.addWidget(mainContent)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    # Phương thức hiển thị thông báo khi nhấn nút
    def show_message(self, message):
        QMessageBox.information(self, message, f"You clicked {message} button")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
