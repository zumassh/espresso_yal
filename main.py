import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_data()
        self.refreshButton.clicked.connect(self.load_data)

    def load_data(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM coffee")
        rows = cur.fetchall()
        self.coffeeTable.setRowCount(len(rows))
        self.coffeeTable.setColumnCount(len(rows[0]))
        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                self.coffeeTable.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        con.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
