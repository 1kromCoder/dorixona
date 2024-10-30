import sys
import pymysql
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QDialog, QFormLayout,
    QLineEdit, QLabel, QMessageBox
)
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="ikromxon03022005",
        database="apteka"
    )
class AddMedicineDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dori Qo'shish")
        self.setGeometry(150, 150, 300, 250)

        self.layout = QFormLayout()

        self.name_input = QLineEdit()
        self.manufacturer_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.price_input = QLineEdit()
        self.expiry_input = QLineEdit()

        self.layout.addRow(QLabel("Nomi:"), self.name_input)
        self.layout.addRow(QLabel("Ishlab Chiqaruvchi:"), self.manufacturer_input)
        self.layout.addRow(QLabel("Miqdor:"), self.quantity_input)
        self.layout.addRow(QLabel("Narx:"), self.price_input)
        self.layout.addRow(QLabel("Amal Qilish Muddati:"), self.expiry_input)

        self.submit_button = QPushButton("Qo'shish")
        self.submit_button.clicked.connect(self.add_medicine)
        self.layout.addRow(self.submit_button)

        self.setLayout(self.layout)

    def add_medicine(self):
        nomi = self.name_input.text()
        ishlab_chiqaruvchi = self.manufacturer_input.text()
        miqdor = self.quantity_input.text()
        narx = self.price_input.text()
        amal_qilish = self.expiry_input.text()

        try:
            connection = connect_db()
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO dorilar (nomi, ishlab_chiqaruvchi, miqdor, narx, amal_qilish) 
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (nomi, ishlab_chiqaruvchi, miqdor, narx, amal_qilish))
            connection.commit()
            QMessageBox.information(self, "Success", "Dori muvaffaqiyatli qo'shildi!")
        except pymysql.MySQLError as err:
            QMessageBox.warning(self, "Xato", f"Xato yuz berdi: {err}")
        finally:
            cursor.close()
            connection.close()
            self.accept()
class AddCustomerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mijoz Qo'shish")
        self.setGeometry(150, 150, 300, 200)

        self.layout = QFormLayout()

        self.name_input = QLineEdit()
        self.surname_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        self.layout.addRow(QLabel("Ism:"), self.name_input)
        self.layout.addRow(QLabel("Familiya:"), self.surname_input)
        self.layout.addRow(QLabel("Telefon Raqam:"), self.phone_input)
        self.layout.addRow(QLabel("Manzil:"), self.address_input)

        self.submit_button = QPushButton("Qo'shish")
        self.submit_button.clicked.connect(self.add_customer)
        self.layout.addRow(self.submit_button)

        self.setLayout(self.layout)

    def add_customer(self):
        ism = self.name_input.text()
        familya = self.surname_input.text()
        telefon_raqam = self.phone_input.text()
        manzil = self.address_input.text()

        try:
            connection = connect_db()
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO mijozlar (ism, familya, telefon_raqam, manzil) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (ism, familya, telefon_raqam, manzil))
            connection.commit()
            QMessageBox.information(self, "Success", "Mijoz muvaffaqiyatli qo'shildi!")
        except pymysql.MySQLError as err:
            QMessageBox.warning(self, "Xato", f"Xato yuz berdi: {err}")
        finally:
            cursor.close()
            connection.close()
            self.accept()
class AddOrderDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buyurtma Qo'shish")
        self.setGeometry(150, 150, 300, 200)

        self.layout = QFormLayout()

        self.customer_id_input = QLineEdit()
        self.medicine_id_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.order_date_input = QLineEdit()

        self.layout.addRow(QLabel("Mijoz ID:"), self.customer_id_input)
        self.layout.addRow(QLabel("Dori ID:"), self.medicine_id_input)
        self.layout.addRow(QLabel("Miqdor:"), self.quantity_input)
        self.layout.addRow(QLabel("Buyurtma Sanasi:"), self.order_date_input)

        self.submit_button = QPushButton("Qo'shish")
        self.submit_button.clicked.connect(self.add_order)
        self.layout.addRow(self.submit_button)

        self.setLayout(self.layout)

    def add_order(self):
        mijoz_id = self.customer_id_input.text()
        dori_id = self.medicine_id_input.text()
        miqdor = self.quantity_input.text()
        buyurtma_sanasi = self.order_date_input.text()

        try:
            connection = connect_db()
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO buyurtmalar (mijoz_id, dori_id, miqdor, buyurtma_sanasi) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (mijoz_id, dori_id, miqdor, buyurtma_sanasi))
            connection.commit()
            QMessageBox.information(self, "Success", "Buyurtma muvaffaqiyatli qo'shildi!")
        except pymysql.MySQLError as err:
            QMessageBox.warning(self, "Xato", f"Xato yuz berdi: {err}")
        finally:
            cursor.close()
            connection.close()
            self.accept()
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apteka Tizimi")
        self.setGeometry(100, 100, 300, 300)

        layout = QVBoxLayout()

        self.add_medicine_button = QPushButton("Dori Qo'shish")
        self.add_medicine_button.clicked.connect(self.open_add_medicine_dialog)

        self.add_customer_button = QPushButton("Mijoz Qo'shish")
        self.add_customer_button.clicked.connect(self.open_add_customer_dialog)

        self.add_order_button = QPushButton("Buyurtma Qo'shish")
        self.add_order_button.clicked.connect(self.open_add_order_dialog)

        layout.addWidget(self.add_medicine_button)
        layout.addWidget(self.add_customer_button)
        layout.addWidget(self.add_order_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_add_medicine_dialog(self):
        dialog = AddMedicineDialog()
        dialog.exec()

    def open_add_customer_dialog(self):
        dialog = AddCustomerDialog()
        dialog.exec()

    def open_add_order_dialog(self):
        dialog = AddOrderDialog()
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())

