# Họ và tên: Phan Nguyễn Thế Vinh
#MSSV: 2100011204
 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QGroupBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Entry Form")
        self.setGeometry(100, 100, 500, 600)  # Đặt kích thước cửa sổ chính

        mainLayout = QVBoxLayout()

        # User Information Group
        userInfoGroup = QGroupBox("Bài tập 3")
        userInfoLayout = QVBoxLayout()

        firstNameLayout = QHBoxLayout()
        firstNameLabel = QLabel("First Name")
        self.firstNameInput = QLineEdit()
        firstNameLayout.addWidget(firstNameLabel)
        firstNameLayout.addWidget(self.firstNameInput)

        lastNameLayout = QHBoxLayout()
        lastNameLabel = QLabel("Last Name")
        self.lastNameInput = QLineEdit()
        lastNameLayout.addWidget(lastNameLabel)
        lastNameLayout.addWidget(self.lastNameInput)

        titleLayout = QHBoxLayout()
        titleLabel = QLabel("Title")
        self.titleInput = QComboBox()
        self.titleInput.addItems(["Mr.", "Ms.", "Dr.", "Prof."])
        titleLayout.addWidget(titleLabel)
        titleLayout.addWidget(self.titleInput)

        ageLayout = QHBoxLayout()
        ageLabel = QLabel("Age")
        self.ageInput = QSpinBox()
        self.ageInput.setRange(0, 100)
        ageLayout.addWidget(ageLabel)
        ageLayout.addWidget(self.ageInput)

        nationalityLayout = QHBoxLayout()
        nationalityLabel = QLabel("Nationality")
        self.nationalityInput = QLineEdit()
        nationalityLayout.addWidget(nationalityLabel)
        nationalityLayout.addWidget(self.nationalityInput)

        userInfoLayout.addLayout(firstNameLayout)
        userInfoLayout.addLayout(lastNameLayout)
        userInfoLayout.addLayout(titleLayout)
        userInfoLayout.addLayout(ageLayout)
        userInfoLayout.addLayout(nationalityLayout)
        userInfoGroup.setLayout(userInfoLayout)

        # Registration Status Group
        registrationGroup = QGroupBox("Registration Status")
        registrationLayout = QVBoxLayout()

        registrationStatusLayout = QHBoxLayout()
        self.registrationCheckbox = QCheckBox("Currently Registered")
        registrationStatusLayout.addWidget(self.registrationCheckbox)

        completedCoursesLayout = QHBoxLayout()
        completedCoursesLabel = QLabel("# Completed Courses")
        self.completedCoursesInput = QSpinBox()
        self.completedCoursesInput.setRange(0, 100)
        completedCoursesLayout.addWidget(completedCoursesLabel)
        completedCoursesLayout.addWidget(self.completedCoursesInput)

        semestersLayout = QHBoxLayout()
        semestersLabel = QLabel("# Semesters")
        self.semestersInput = QSpinBox()
        self.semestersInput.setRange(0, 20)
        semestersLayout.addWidget(semestersLabel)
        semestersLayout.addWidget(self.semestersInput)

        registrationLayout.addLayout(registrationStatusLayout)
        registrationLayout.addLayout(completedCoursesLayout)
        registrationLayout.addLayout(semestersLayout)
        registrationGroup.setLayout(registrationLayout)

        # Terms & Conditions Group
        termsGroup = QGroupBox("Terms & Conditions")
        termsLayout = QVBoxLayout()
        self.termsCheckbox = QCheckBox("I accept the terms and conditions.")
        termsLayout.addWidget(self.termsCheckbox)
        termsGroup.setLayout(termsLayout)

        # Submit Button
        submitButton = QPushButton("Enter data")
        submitButton.clicked.connect(self.submitData)

        # Add groups to main layout
        mainLayout.addWidget(userInfoGroup)
        mainLayout.addWidget(registrationGroup)
        mainLayout.addWidget(termsGroup)
        mainLayout.addWidget(submitButton)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

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
