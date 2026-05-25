import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt6 import uic



class ConfigDialog(QDialog):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("Config_dialog_box.ui",self)

        # --- initialise variables
        self.team_one_name = ""
        self.team_two_name = ""

        self.button_one_value = 3
        self.button_two_value = 1
        self.button_three_value = -1

        self.timer_minutes = 0
        self.timer_seconds = 0
        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.pushButton_save_names.clicked.connect(self.accept_changes_names)
        self.pushButton_save_buttons.clicked.connect(self.accept_changes_buttons)
        self.pushButton_save_timer.clicked.connect(self.accept_changes_timer)

    # ---- SLOTS ---- #

    # Names ---------
    def accept_changes_names(self):
        self.team_one_name = self.lineEdit_team_one.text()
        self.team_two_name = self.lineEdit_team_two.text()
        self.save_changes_names()

    def save_changes_names(self):
        self.team_one_name = self.lineEdit_team_one.text()
        self.team_two_name = self.lineEdit_team_two.text()
    
    # Buttons ---------
    def accept_changes_buttons(self):
        self.button_one_value = int(self.spinBox_button_1.text())
        self.button_two_value = int(self.spinBox_button_2.text())
        self.button_three_value = int(self.spinBox_button_3.text())
        self.save_changes_buttons()
    
    def save_changes_buttons(self):
        self.button_one_value = int(self.spinBox_button_1.text())
        self.button_two_value = int(self.spinBox_button_2.text())
        self.button_three_value = int(self.spinBox_button_3.text())

    # Timer ---------
    def accept_changes_timer(self):
        self.timer_minutes = int(self.spinBox_minutes.text())
        self.timer_seconds = int(self.spinBox_seconds.text())
        self.save_changes_timer()

    def save_changes_timer(self):
        self.timer_minutes = int(self.spinBox_minutes.text())
        self.timer_seconds = int(self.spinBox_seconds.text())

    #---- further processing ----#
    def get_button_values(self):
        return self.button_one_value, self.button_two_value, self.button_three_value

    def get_timer_values(self):
        return self.timer_minutes, self.timer_seconds

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigDialog()
    window.show()
    sys.exit(app.exec())
