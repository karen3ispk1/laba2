from math import sqrt
from PySide6 import QtCore, QtGui, QtWidgets
import spacy
import sys

nlp = spacy.load('en_core_web_md')

def squared_sum(x):
  """ return 3 rounded square rooted value """
 
  return round(sqrt(sum([a*a for a in x])),3)

def cos_similarity(x,y):
  """ return cosine similarity between two lists """
 
  numerator = sum(a*b for a,b in zip(x,y))
  denominator = squared_sum(x)*squared_sum(y)
  return round(numerator/float(denominator),3)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
       super().__init__()
       self.__init_ui()
       self.__setting_ui()
       self.show()

    def __init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_v_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.text_line_edit_one = QtWidgets.QTextEdit()
        self.text_line_edit_two = QtWidgets.QTextEdit()
        self.spin_box = QtWidgets.QSpinBox()
        self.check_button = QtWidgets.QPushButton('Check')

    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)

        self.spin_box.setMinimum(0)
        self.spin_box.setMaximum(100)
        # self.spin_box.setSingleStep(5)
        self.spin_box.setSuffix('%')

        self.text_line_edit_one.setPlaceholderText('Entry one text')
        self.text_line_edit_two.setPlaceholderText('Entry two text')

        self.main_v_layout.addWidget(self.text_line_edit_one)
        self.main_v_layout.addWidget(self.text_line_edit_two)
        self.main_v_layout.addWidget(self.spin_box)
        self.main_v_layout.addWidget(self.check_button)

        self.check_button.clicked.connect(self.on_check_button_click)
    
    def on_check_button_click(self) -> None:
        embeddings = [nlp(sentence).vector for sentence in (self.text_line_edit_one.toPlainText(), self.text_line_edit_two.toPlainText())]
        self.statusBar().showMessage('Plagiated') if cos_similarity(embeddings[0], embeddings[1]) * 100 > int(self.spin_box.text().replace('%', '')) else self.statusBar().showMessage('Not plagiated')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = MainWindow()
    app.exec()

