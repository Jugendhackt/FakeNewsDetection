import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QGridLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import search


class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Suchfeld mit Suchbutton')
        self.setFixedSize(900, 600)

        # Label und Eingabefeld für die Suche
        self.search_label = QLabel('Suche:')
        self.search_input = QLineEdit()

        # Button zum Starten der Suche
        self.search_button = QPushButton(QIcon('search.png'), 'Suchen')
        self.search_button.clicked.connect(self.search)

        # Eingabefeld soll auf Return reagieren
        self.search_input.returnPressed.connect(self.search)

        self.list_widget = QListWidget()
        self.list_widget.setFont(QFont("Helvetica", 14)) # Schriftart und -größe ändern
        self.list_widget.setStyleSheet("background-color: #f5f5f5; color: #333") # Hintergrundfarbe und Schriftfarbe anpassen

        # Layout
        layout = QGridLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setVerticalSpacing(30)
        layout.addWidget(self.search_label, 0, 0, Qt.AlignRight)
        layout.addWidget(self.search_input, 0, 1)
        layout.addWidget(self.search_button, 0, 2)
        layout.addWidget(self.list_widget, 1, 0, 1, 3)

        self.list_widget.hide()

        self.setLayout(layout)
        self.show()

    def search(self):
        # Suche ausführen und Ergebnis ausgeben
        search_term = self.search_input.text()
        search_results = search.search_(search_term)

        for i in range(len(search_results)):
            self.list_widget.addItem(search_results[i])

        self.search_label.hide()
        self.search_input.hide()
        self.search_button.hide()

        self.list_widget.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_window = SearchWindow()
    sys.exit(app.exec_())
