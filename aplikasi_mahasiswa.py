import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QLineEdit, QHBoxLayout, QGroupBox, QSpinBox, QDoubleSpinBox

class StudentDashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Student Dashboard')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label_welcome = QLabel('Selamat Datang di Dashboard Mahasiswa_STMIK JAYAKARTA')
        self.layout.addWidget(self.label_welcome)

        self.student_name_input = QLineEdit()
        self.student_name_input.setPlaceholderText('Masukkan Nama Mahasiswa')
        self.layout.addWidget(self.student_name_input)

        self.course_inputs_group = QGroupBox('Masukkan Nama Matakuliah, SKS, dan Nilai')
        self.course_inputs_layout = QVBoxLayout()

        self.course_fields = []
        for i in range(4):  # Misalnya, kita akan memasukkan 4 matakuliah
            hbox = QHBoxLayout()
            course_label = QLabel(f'Matakuliah {i + 1}: ')
            course_input = QLineEdit()
            sks_input = QSpinBox()
            sks_input.setMinimum(1)
            sks_input.setMaximum(6)
            grade_input = QDoubleSpinBox()
            grade_input.setMinimum(0)
            grade_input.setMaximum(100)
            hbox.addWidget(course_label)
            hbox.addWidget(course_input)
            hbox.addWidget(QLabel('SKS:'))
            hbox.addWidget(sks_input)
            hbox.addWidget(QLabel('Nilai:'))
            hbox.addWidget(grade_input)
            self.course_fields.append((course_input, sks_input, grade_input))
            self.course_inputs_layout.addLayout(hbox)

        self.course_inputs_group.setLayout(self.course_inputs_layout)
        self.layout.addWidget(self.course_inputs_group)

        self.btn_view_grades = QPushButton('Lihat Nilai')
        self.btn_view_grades.clicked.connect(self.view_grades)
        self.layout.addWidget(self.btn_view_grades)

    def view_grades(self):
        student_name = self.student_name_input.text()
        course_grades = []
        total_grade = 0
        total_sks = 0
        for field in self.course_fields:
            course_name = field[0].text()
            sks = field[1].value()
            grade = field[2].value()
            total_sks += sks
            course_grades.append((course_name, sks, grade))
            total_grade += grade

        grade_message = f"Nama Mahasiswa: {student_name}\nDaftar Nilai Matakuliah:\n"
        for course, sks, grade in course_grades:
            grade_message += f"{course} (SKS: {sks}): {grade}\n"

        average_grade = total_grade / len(self.course_fields) if len(self.course_fields) > 0 else 0
        gpa = total_grade / total_sks if total_sks > 0 else 0

        grade_message += f"\nIPK: {gpa:.2f}\nRata-rata Nilai: {average_grade:.2f}"

        QMessageBox.information(self, 'Nilai Mahasiswa', grade_message)

def main():
    app = QApplication(sys.argv)
    window = StudentDashboard()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
