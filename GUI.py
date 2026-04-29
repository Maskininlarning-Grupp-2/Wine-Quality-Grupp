import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QTextEdit, QLabel, \
    QGridLayout, QLineEdit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Wine Quality Prediction')
        self.setFixedSize(400, 600)
        # Layout
        layout = QGridLayout()

        # Widgets
        fixed_acidity = QLineEdit()
        fixed_acidity.setValidator(QDoubleValidator())
        fixed_acidity.setFixedSize(150, 30)
        fixed_acidity_title = QLabel('Fixed acidity')

        volatile_acidity = QLineEdit()
        volatile_acidity.setValidator(QDoubleValidator())
        volatile_acidity.setFixedSize(150, 30)
        volatile_acidity_title = QLabel('Volatile acidity')

        citric_acid = QLineEdit()
        citric_acid.setValidator(QDoubleValidator())
        citric_acid.setFixedSize(150, 30)
        citric_acid_title = QLabel('Citric acid')

        residual_sugar = QLineEdit()
        residual_sugar.setValidator(QDoubleValidator())
        residual_sugar.setFixedSize(150, 30)
        residual_sugar_title = QLabel('Residual sugar')

        chlorides = QLineEdit()
        chlorides.setValidator(QDoubleValidator())
        chlorides.setFixedSize(150, 30)
        chlorides_title = QLabel('Chlorides')

        free_sulfur_dioxide = QLineEdit()
        free_sulfur_dioxide.setValidator(QDoubleValidator())
        free_sulfur_dioxide.setFixedSize(150, 30)
        free_sulfur_dioxide_title = QLabel('Free sulfur dioxide')


        total_sulfur_dioxide = QLineEdit()
        total_sulfur_dioxide.setValidator(QDoubleValidator())
        total_sulfur_dioxide.setFixedSize(150, 30)
        total_sulfur_dioxide_title = QLabel('Total sulfur dioxide')

        density = QLineEdit()
        density.setValidator(QDoubleValidator())
        density.setFixedSize(150, 30)
        density_title = QLabel('Density')

        pH = QLineEdit()
        pH.setValidator(QDoubleValidator())
        pH.setFixedSize(150, 30)
        pH_title = QLabel('PH')

        sulphates = QLineEdit()
        sulphates.setValidator(QDoubleValidator())
        sulphates.setFixedSize(150, 30)
        sulphates_title = QLabel('Sulphates')

        alcohol = QLineEdit()
        alcohol.setValidator(QDoubleValidator())
        alcohol.setFixedSize(150, 30)
        alcohol_title = QLabel('Alcohol')

        # Buttons
        support_vector_machine = QPushButton('SVM')
        support_vector_machine.setFixedSize(150, 30)
        decision_tree = QPushButton('Decision Tree')
        decision_tree.setFixedSize(150, 30)
        random_forest = QPushButton('Random Forest')
        random_forest.setFixedSize(150, 30)
        logistic_regression = QPushButton('Logistic Regression')
        logistic_regression.setFixedSize(150, 30)

        # layout handling
        layout.addWidget(fixed_acidity_title, 0, 0)
        layout.addWidget(fixed_acidity, 1, 0)

        layout.addWidget(volatile_acidity_title, 2, 0)
        layout.addWidget(volatile_acidity, 3, 0)

        layout.addWidget(citric_acid_title, 4, 0)
        layout.addWidget(citric_acid, 5, 0)

        layout.addWidget(residual_sugar_title, 6, 0)
        layout.addWidget(residual_sugar, 7, 0)

        layout.addWidget(chlorides_title, 8, 0)
        layout.addWidget(chlorides, 9, 0)

        layout.addWidget(free_sulfur_dioxide_title, 10, 0)
        layout.addWidget(free_sulfur_dioxide, 11, 0)

        layout.addWidget(total_sulfur_dioxide_title, 0, 1)
        layout.addWidget(total_sulfur_dioxide, 1, 1)

        layout.addWidget(density_title, 2, 1)
        layout.addWidget(density, 3, 1)

        layout.addWidget(pH_title, 4, 1)
        layout.addWidget(pH, 5, 1)

        layout.addWidget(sulphates_title, 6, 1)
        layout.addWidget(sulphates, 7, 1)

        layout.addWidget(alcohol_title, 8, 1)
        layout.addWidget(alcohol, 9, 1)

        layout.addWidget(logistic_regression, 12, 0)
        layout.addWidget(support_vector_machine, 12, 1)

        layout.addWidget(decision_tree, 13, 0)
        layout.addWidget(random_forest, 13, 1)



        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
app = QApplication(sys.argv)

window = Window()

window.show()