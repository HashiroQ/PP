import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from image_operations import process_image

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Resizer & Rotator")
        self.setGeometry(300, 200, 600, 400)

        self.initUI()

    def initUI(self):
        # Центральный виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создание элементов интерфейса
        self.image_label = QLabel("Выберите изображение", self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.width_input = QLineEdit(self)
        self.width_input.setPlaceholderText("Введите новую ширину")

        self.height_input = QLineEdit(self)
        self.height_input.setPlaceholderText("Введите новую высоту")

        self.rotation_input = QLineEdit(self)
        self.rotation_input.setPlaceholderText("Введите угол поворота (градусы)")

        self.choose_button = QPushButton("Выбрать изображение", self)
        self.choose_button.clicked.connect(self.open_file_dialog)

        self.process_button = QPushButton("Обработать изображение", self)
        self.process_button.clicked.connect(self.process_image)

        # Компоновка элементов
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.width_input)
        layout.addWidget(self.height_input)
        layout.addWidget(self.rotation_input)
        layout.addWidget(self.choose_button)
        layout.addWidget(self.process_button)

        central_widget.setLayout(layout)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))

    def process_image(self):
        try:
            new_width = int(self.width_input.text())
            new_height = int(self.height_input.text())
            rotation_angle = int(self.rotation_input.text())
            processed_path = process_image(self.image_path, new_width, new_height, rotation_angle)
            pixmap = QPixmap(processed_path)
            self.image_label.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))
        except Exception as e:
            self.image_label.setText(f"Ошибка: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
