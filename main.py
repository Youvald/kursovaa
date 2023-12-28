from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
from new_contract_ui import Ui_MainWindow

class NewContractWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NewContractWindow, self).__init__()
        self.setupUi(self)

        # Встановлення початкової дати як поточної дати
        current_date = QDate.currentDate()
        self.dateEdit.setDate(current_date)
        self.dateEdit_2.setDate(current_date)

        # Підключення обробників подій до зміни дати для обох віджетів
        self.dateEdit.dateChanged.connect(self.on_date_changed)
        self.dateEdit_2.dateChanged.connect(self.on_date_changed)

        # Підключення обробників подій для QComboBox і QCheckBox
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.checkBox.stateChanged.connect(self.on_checkbox_changed)

        # Підключення обробника події для кнопки "Send"
        self.create_contract.pressed.connect(self.on_create_contract_clicked)

        # Ініціалізація ціни
        self.update_price()


    def on_date_changed(self):
        # Обробка події зміни дати
        # Отримання об'єктів дат і обчислення різниці між ними
        start_date = self.dateEdit.date()
        end_date = self.dateEdit_2.date()
        days_difference = (end_date.toPyDate() - start_date.toPyDate()).days

        # Оновлення тексту в QLabel для відображення кількості днів
        self.label.setText(f"{days_difference} days")

        # Оновлення ціни
        self.update_price()

    def on_combobox_changed(self):
        # Обробка події зміни вмісту QComboBox
        # Оновлення ціни
        self.update_price()

    def on_checkbox_changed(self):
        # Обробка події зміни стану QCheckBox
        # Оновлення ціни
        self.update_price()

    def update_price(self):
        # Отримання вибраних значень
        selected_ad_space = self.comboBox.currentText()
        has_design = self.checkBox.isChecked()

        # Отримання кількості днів
        start_date = self.dateEdit.date()
        end_date = self.dateEdit_2.date()
        number_of_days = (end_date.toPyDate() - start_date.toPyDate()).days

        # Обчислення ціни
        price = self.calculate_price(selected_ad_space, has_design, number_of_days)

        # Оновлення тексту в QLabel для відображення ціни
        self.label.setText(f"{max(price, 0)}$")

    def calculate_price(self, ad_space, has_design, number_of_days):
        # Логіка для розрахунку ціни в залежності від місця розміщення та наявності дизайну
        base_price = 0

        if ad_space == "Metro":
            base_price = 50
        elif ad_space == "Radio":
            base_price = 10
        elif ad_space == "TV":
            base_price = 100
        elif ad_space == "Transport":
            base_price = 30
        elif ad_space == "Billboard":
            base_price = 25

        # Додаткова плата за відсутність дизайну
        additional_design_fee = 100 if not has_design else 0

        # Розрахунок загальної ціни на основі кількості днів
        total_price = (base_price * number_of_days) + additional_design_fee

        return total_price

    def on_create_contract_clicked(self):
        # Обробник події натискання кнопки "create_contract"
        total_price = self.calculate_price(self.comboBox.currentText(),
                                           self.checkBox.isChecked(),
                                           (self.dateEdit_2.date().toPyDate() - self.dateEdit.date().toPyDate()).days)

        # Відображення повідомлення з обраною ціною
        QMessageBox.information(self, "Contract Created",
                                f"Contract created successfully!\nTotal Price: {max(total_price, 0)}$")




if __name__ == '__main__':
    app = QApplication([])
    window = NewContractWindow()
    window.show()
    app.exec_()
