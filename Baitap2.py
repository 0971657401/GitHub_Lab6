# Họ và tên: Phan Nguyễn Thế Vinh
# MSSV: 2100011204

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bài tập 2")
        self.setGeometry(100, 100, 900, 600)  # Đặt kích thước cửa sổ chính

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
            }
            QPushButton:hover {
                background-color: #ff00ff;
            }
            QPushButton:pressed {
                background-color: #cc00cc;
            }
        """)

        # Sidebar layout
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #C0C0C0; color: white;")

        self.statusLabel = QLabel("AtarBals AntiVirus")
        self.statusLabel.setAlignment(Qt.AlignLeft)
        self.statusLabel.setStyleSheet("font-size: 20px; padding: 20px; font-weight: bold; color: black;")

        self.statusButton = QPushButton("Status")
        self.statusButton.setStyleSheet("background-color: #1E90FF; color: white;")
        self.updateButton = QPushButton("Updates")
        self.updateButton.setStyleSheet("background-color: #32CD32; color: white;")
        self.settingsButton = QPushButton("Settings")
        self.settingsButton.setStyleSheet("background-color: #FF8C00; color: white;")
        self.feedbackButton = QPushButton("Share Feedback")
        self.feedbackButton.setStyleSheet("background-color: #DA70D6; color: white;")
        self.premiumButton = QPushButton("Buy Premium")
        self.premiumButton.setStyleSheet("background-color: #8B0000; color: white;")
        self.helpButton = QPushButton("Help")
        self.helpButton.setStyleSheet("background-color: #4B0082; color: white;")
        self.scanNowButton = QPushButton("Scan Now")
        self.scanNowButton.setStyleSheet("background-color: #00FF00; color: black; border: 2px solid black;")

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

        # Main content layout
        self.titleLabel = QLabel("Scan")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.subtitleLabel = QLabel("Premium will be free forever. You just need to click button.")
        self.subtitleLabel.setAlignment(Qt.AlignCenter)
        self.subtitleLabel.setStyleSheet("font-size: 16px; color: white;")

        self.quickScanButton = QPushButton("Quick Scan")
        self.quickScanButton.setStyleSheet("background-color: white; color: black; border: 2px solid black;")
        self.webProtectionButton = QPushButton("Web Protection")
        self.webProtectionButton.setStyleSheet("background-color: white; color: black; border: 2px solid black;")
        self.quarantineButton = QPushButton("Quarantine")
        self.quarantineButton.setStyleSheet("background-color: white; color: black; border: 2px solid black;")
        self.fullScanButton = QPushButton("Full Scan")
        self.fullScanButton.setStyleSheet("background-color: white; color: black; border: 2px solid black;")
        self.simpleUpdateButton = QPushButton("Simple Update")
        self.simpleUpdateButton.setStyleSheet("background-color: white; color: black; border: 2px solid black;")

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

        # Main layout
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.sidebar)
        mainLayout.addWidget(mainContent)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
