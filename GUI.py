import sys

import joblib
import pandas as pd
from PyQt6.QtCore import Qt, QLocale
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QTextEdit, QLabel, \
    QGridLayout, QLineEdit, QMessageBox, QDialog
from pandas import DataFrame

demo_mode = True

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Wine Quality Prediction')
        self.setFixedSize(400, 600)
        validator = QDoubleValidator(0.0, 100.0, 5)
        locale = QLocale(QLocale.Language.English)
        validator.setLocale(locale)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        # Layout
        layout = QGridLayout()

        # Widgets
        fixed_acidity = QLineEdit()
        fixed_acidity.setValidator(validator)
        fixed_acidity.setFixedSize(150, 30)
        fixed_acidity_title = QLabel('Fixed acidity')

        volatile_acidity = QLineEdit()
        volatile_acidity.setValidator(validator)
        volatile_acidity.setFixedSize(150, 30)
        volatile_acidity_title = QLabel('Volatile acidity')

        citric_acid = QLineEdit()
        citric_acid.setValidator(validator)
        citric_acid.setFixedSize(150, 30)
        citric_acid_title = QLabel('Citric acid')

        residual_sugar = QLineEdit()
        residual_sugar.setValidator(validator)
        residual_sugar.setFixedSize(150, 30)
        residual_sugar_title = QLabel('Residual sugar')

        chlorides = QLineEdit()
        chlorides.setValidator(validator)
        chlorides.setFixedSize(150, 30)
        chlorides_title = QLabel('Chlorides')

        free_sulfur_dioxide = QLineEdit()
        free_sulfur_dioxide.setValidator(validator)
        free_sulfur_dioxide.setFixedSize(150, 30)
        free_sulfur_dioxide_title = QLabel('Free sulfur dioxide')


        total_sulfur_dioxide = QLineEdit()
        total_sulfur_dioxide.setValidator(validator)
        total_sulfur_dioxide.setFixedSize(150, 30)
        total_sulfur_dioxide_title = QLabel('Total sulfur dioxide')

        density = QLineEdit()
        density.setValidator(validator)
        density.setFixedSize(150, 30)
        density_title = QLabel('Density')

        pH = QLineEdit()
        pH.setValidator(validator)
        pH.setFixedSize(150, 30)
        pH_title = QLabel('PH')

        sulphates = QLineEdit()
        sulphates.setValidator(validator)
        sulphates.setFixedSize(150, 30)
        sulphates_title = QLabel('Sulphates')

        alcohol = QLineEdit()
        alcohol.setValidator(validator)
        alcohol.setFixedSize(150, 30)
        alcohol_title = QLabel('Alcohol')

        self.pred_results = QTextEdit()
        self.pred_results.setFixedSize(150, 160)
        self.pred_results.setReadOnly(True)
        self.pred_results_title = QLabel('Prediction results: ')

        # Buttons
        input_data = QPushButton('Input Data')
        input_data.setFixedSize(150, 30)
        input_data.clicked.connect(lambda: self.create_data(fixed_acidity.text(), volatile_acidity.text(), citric_acid.text(), residual_sugar.text(), chlorides.text(), free_sulfur_dioxide.text(), total_sulfur_dioxide.text(), density.text(), pH.text(), sulphates.text(), alcohol.text()))

        if demo_mode:
            fixed_acidity.setText('7.4')
            volatile_acidity.setText('0.700')
            citric_acid.setText('0.0')
            residual_sugar.setText('1.9')
            chlorides.setText('0.076')
            free_sulfur_dioxide.setText('11.0')
            total_sulfur_dioxide.setText('34.0')
            sulphates.setText('0.56')
            density.setText('0.99780')
            pH.setText('3.51')
            alcohol.setText('9.4')

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

        layout.addWidget(input_data, 12, 0)
        layout.addWidget(self.pred_results_title, 10, 1)
        layout.addWidget(self.pred_results, 11, 1, 2, 0)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def create_data(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
        data = {
            'fixed acidity': [fixed_acidity],
            'volatile acidity': [volatile_acidity],
            'citric acid': [citric_acid],
            'residual sugar': [residual_sugar],
            'chlorides': [chlorides],
            'free sulfur dioxide': [free_sulfur_dioxide],
            'total sulfur dioxide': [total_sulfur_dioxide],
            'density': [density],
            'pH': [pH],
            'sulphates': [sulphates],
            'alcohol': [alcohol]
        }
        try:
            dlg = ModelBox(pd.DataFrame(data))
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
        if dlg.exec():
            try:
                self.pred_results_title.setText(dlg.pred()[0])
                self.pred_results.setText(f"Quality Prediction: {dlg.pred()[1][0]}\n"
                                          f"---Accuracy Data---\n"
                                          f"Likelihood of 3: {dlg.pred()[2][0][0]}\n"
                                          f"Likelihood of 4: {dlg.pred()[2][0][1]}\n"
                                          f"Likelihood of 5: {dlg.pred()[2][0][2]}\n"
                                          f"Likelihood of 6: {dlg.pred()[2][0][3]}\n"
                                          f"Likelihood of 7: {dlg.pred()[2][0][4]}\n"
                                          f"Likelihood of 8: {dlg.pred()[2][0][5]}\n")
            except Exception:
                QMessageBox.warning(self, "Error", "Data input empty or faulty!")

class ModelBox(QDialog):
    prediction_data = []
    def __init__(self, df: DataFrame):
        super().__init__()
        self.df = df

        self.setWindowTitle("Select Algorithm")

        layout = QVBoxLayout()
        support_vector_machine = QPushButton('SVM')
        support_vector_machine.clicked.connect(lambda: self.model_predict("svm"))
        support_vector_machine.clicked.connect(self.accept)

        decision_tree = QPushButton('Decision Tree')
        decision_tree.clicked.connect(lambda: self.model_predict("decision_tree"))
        decision_tree.clicked.connect(self.accept)

        random_forest = QPushButton('Random Forest')
        random_forest.clicked.connect(lambda: self.model_predict("random_forest"))
        random_forest.clicked.connect(self.accept)

        logistic_regression = QPushButton('Logistic Regression')
        logistic_regression.clicked.connect(lambda: self.model_predict("logistic_regression"))
        logistic_regression.clicked.connect(self.accept)

        layout.addWidget(support_vector_machine)
        layout.addWidget(decision_tree)
        layout.addWidget(random_forest)
        layout.addWidget(logistic_regression)

        self.setLayout(layout)
    def model_predict(self, algorithm):
        self.prediction_data.clear()
        try:
            clf = joblib.load(f'./models/{algorithm}.pkl')
            self.prediction_data.append(algorithm.replace('_', ' ').upper())
            self.prediction_data.append(clf.predict(self.df.values))
            self.prediction_data.append(clf.predict_proba(self.df.values))
        except Exception as e:
            pass
    def pred(self):
        return self.prediction_data


app = QApplication(sys.argv)

window = Window()

window.show()