import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import search

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Suchfeld mit Suchbutton')

        # Label und Eingabefeld für die Suche
        search_label = QLabel('Suche:')
        self.search_input = QLineEdit()
        # Button zum Starten der Suche
        search_button = QPushButton('Suchen')
        search_button.clicked.connect(self.search)

        # Eingabefeld soll auf Return reagieren
        self.search_input.returnPressed.connect(self.search)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(search_button)

        self.setLayout(layout)
        self.show()

    def search(self):
        # Suche ausführen und Ergebnis ausgeben
        search_term = self.search_input.text()
        print(f'Suche nach "{search.search_(search_term)}" gestartet.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_window = SearchWindow()
    sys.exit(app.exec_())
