import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMessageBox


class AddEditCoffeeForm(QDialog):
    def __init__(self, coffee_id=None):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.coffee_id = coffee_id
        self.saveButton.clicked.connect(self.save_data)
        if self.coffee_id:
            self.load_coffee_data()

    def load_coffee_data(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute("SELECT name, roast_degree, ground_or_beans, b, price, package_volume FROM coffee WHERE id=?", (self.coffee_id,))
        coffee = cur.fetchone()
        con.close()
        if coffee:
            self.nameEdit.setText(coffee[0])
            self.roastEdit.setText(coffee[1])
            self.typeEdit.setText(coffee[2])
            self.descEdit.setText(coffee[3])
            self.priceEdit.setText(str(coffee[4]))
            self.volumeEdit.setText(str(coffee[5]))

    def save_data(self):
        name = self.nameEdit.text()
        roast_degree = self.roastEdit.text()
        ground_or_beans = self.typeEdit.text()
        taste_description = self.descEdit.text()
        price = self.priceEdit.text()
        package_volume = self.volumeEdit.text()

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()

        if self.coffee_id:
            cur.execute('''
                UPDATE coffee
                SET name=?, roast_degree=?, ground_or_beans=?, b=?, price=?, package_volume=?
                WHERE id=?
            ''', (name, roast_degree, ground_or_beans, taste_description, price, package_volume, self.coffee_id))
        else:
            cur.execute('''
                INSERT INTO coffee (name, roast_degree, ground_or_beans, b, price, package_volume)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, roast_degree, ground_or_beans, taste_description, price, package_volume))

        con.commit()
        con.close()
        self.close()
