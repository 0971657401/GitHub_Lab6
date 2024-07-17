# Họ và tên: Phan Nguyễn Thế Vinh
#MSSV: 2100011204

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QGroupBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Entry Form")
        self.setGeometry(100, 100, 500, 600)  # Đặt kích thước cửa sổ chính

        # Đặt kiểu giao diện bằng CSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QGroupBox {
                font-size: 18px;
                font-weight: bold;
                background-color: #E6E6FA;
                border: 2px solid #8A2BE2;
                border-radius: 10px;
                margin-top: 10px;
            }
            QLabel {
                font-size: 16px;
                color: #333;
                margin-bottom: 8px;
            }
            QLineEdit, QComboBox, QSpinBox {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #8A2BE2;
                border-radius: 5px;
                margin-bottom: 8px;
            }
            QCheckBox {
                font-size: 16px;
                margin-bottom: 8px;
            }
            QPushButton {
                font-size: 18px;
                background-color: #8A2BE2;
                color: white;
                border: 2px solid #8A2BE2;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5D3FD3;
                border-color: #5D3FD3;
            }
        """)

        mainLayout = QVBoxLayout()

        # Nhóm thông tin người dùng
        userInfoGroup = QGroupBox("")
        userInfoLayout = QVBoxLayout()

        # Bố trí cho phần nhập tên
        firstNameLayout = QHBoxLayout()
        firstNameLabel = QLabel("First Name")
        self.firstNameInput = QLineEdit()
        firstNameLayout.addWidget(firstNameLabel)
        firstNameLayout.addWidget(self.firstNameInput)

        # Bố trí cho phần nhập họ
        lastNameLayout = QHBoxLayout()
        lastNameLabel = QLabel("Last Name")
        self.lastNameInput = QLineEdit()
        lastNameLayout.addWidget(lastNameLabel)
        lastNameLayout.addWidget(self.lastNameInput)

        # Bố trí cho phần chọn danh hiệu
        titleLayout = QHBoxLayout()
        titleLabel = QLabel("Title")
        self.titleInput = QComboBox()
        self.titleInput.addItems(["Mr.", "Ms.", "Dr.", "Prof."])
        titleLayout.addWidget(titleLabel)
        titleLayout.addWidget(self.titleInput)

        # Bố trí cho phần nhập tuổi
        ageLayout = QHBoxLayout()
        ageLabel = QLabel("Age")
        self.ageInput = QSpinBox()
        self.ageInput.setRange(0, 100)
        ageLayout.addWidget(ageLabel)
        ageLayout.addWidget(self.ageInput)

        # Bố trí cho phần nhập quốc tịch
        nationalityLayout = QHBoxLayout()
        nationalityLabel = QLabel("Nationality")
        self.nationalityInput = QLineEdit()
        nationalityLayout.addWidget(nationalityLabel)
        nationalityLayout.addWidget(self.nationalityInput)

        # Thêm các phần tử vào nhóm thông tin người dùng
        userInfoLayout.addLayout(firstNameLayout)
        userInfoLayout.addLayout(lastNameLayout)
        userInfoLayout.addLayout(titleLayout)
        userInfoLayout.addLayout(ageLayout)
        userInfoLayout.addLayout(nationalityLayout)
        userInfoGroup.setLayout(userInfoLayout)

        # Nhóm trạng thái đăng ký
        registrationGroup = QGroupBox("")
        registrationLayout = QVBoxLayout()

        # Bố trí cho phần chọn trạng thái đăng ký
        registrationStatusLayout = QHBoxLayout()
        self.registrationCheckbox = QCheckBox("Currently Registered")
        registrationStatusLayout.addWidget(self.registrationCheckbox)

        # Bố trí cho phần nhập số khóa học đã hoàn thành
        completedCoursesLayout = QHBoxLayout()
        completedCoursesLabel = QLabel("# Completed Courses")
        self.completedCoursesInput = QSpinBox()
        self.completedCoursesInput.setRange(0, 100)
        completedCoursesLayout.addWidget(completedCoursesLabel)
        completedCoursesLayout.addWidget(self.completedCoursesInput)

        # Bố trí cho phần nhập số học kỳ
        semestersLayout = QHBoxLayout()
        semestersLabel = QLabel("# Semesters")
        self.semestersInput = QSpinBox()
        self.semestersInput.setRange(0, 20)
        semestersLayout.addWidget(semestersLabel)
        semestersLayout.addWidget(self.semestersInput)

        # Thêm các phần tử vào nhóm trạng thái đăng ký
        registrationLayout.addLayout(registrationStatusLayout)
        registrationLayout.addLayout(completedCoursesLayout)
        registrationLayout.addLayout(semestersLayout)
        registrationGroup.setLayout(registrationLayout)

        # Nhóm điều khoản và điều kiện
        termsGroup = QGroupBox("")
        termsLayout = QVBoxLayout()
        self.termsCheckbox = QCheckBox("I accept the terms and conditions.")
        termsLayout.addWidget(self.termsCheckbox)
        termsGroup.setLayout(termsLayout)

        # Nút gửi dữ liệu
        submitButton = QPushButton("Enter data")
        submitButton.clicked.connect(self.submitData)

        # Thêm các nhóm vào bố trí chính
        mainLayout.addWidget(userInfoGroup)
        mainLayout.addWidget(registrationGroup)
        mainLayout.addWidget(termsGroup)
        mainLayout.addWidget(submitButton, alignment=Qt.AlignCenter)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    # Phương thức xử lý khi gửi dữ liệu
    def submitData(self):
        print("First Name:", self.firstNameInput.text())
        print("Last Name:", self.lastNameInput.text())
        print("Title:", self.titleInput.currentText())
        print("Age:", self.ageInput.value())
        print("Nationality:", self.nationalityInput.text())
        print("Currently Registered:", self.registrationCheckbox.isChecked())
        print("# Completed Courses:", self.completedCoursesInput.value())
        print("# Semesters:", self.semestersInput.value())
        print("Terms Accepted:", self.termsCheckbox.isChecked())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
