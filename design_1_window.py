import sys
from tkinter import dialog
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from config_box_window import ConfigDialog
import config_box_window
import time
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("design_1.ui",self)

        # --- initialise variables
        self.timer_minutes = 0
        self.timer_seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)
        self.paused = False

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.pushButton_t1_b1.clicked.connect(self.button_b1_clicked)
        self.pushButton_t2_b1.clicked.connect(self.button_b1_clicked)
        self.pushButton_t1_b2.clicked.connect(self.button_b2_clicked)
        self.pushButton_t2_b2.clicked.connect(self.button_b2_clicked)
        self.pushButton_t1_b3.clicked.connect(self.button_b3_clicked)
        self.pushButton_t2_b3.clicked.connect(self.button_b3_clicked)

        self.pushButton_team_one_reset.clicked.connect(self.button_reset_score_clicked)
        self.pushButton_team_two_reset.clicked.connect(self.button_reset_score_clicked)

        self.pushButton_edit.clicked.connect(self.button_edit_clicked)
        self.pushButton_start.clicked.connect(self.start_button_clicked)
        self.pushButton_stop.clicked.connect(self.stop_button_clicked)
        self.pushButton_pause.clicked.connect(self.pause_button_clicked)
        self.pushButton_reset.clicked.connect(self.reset_button_clicked)

    # ---- SLOTS ---- #
    def button_b1_clicked(self):
        pass

    def button_b2_clicked(self):
        pass

    def button_b3_clicked(self):
        pass

    def button_reset_score_clicked(self):
        pass

    def button_edit_clicked(self):
        window = ConfigDialog()

        if window.exec():
            self.label_team_one.setText(window.team_one_name)
            self.label_team_two.setText(window.team_two_name)

            self.update_button_values(window)

            self.default_minutes = window.timer_minutes
            self.default_seconds = window.timer_seconds

            self.timer_minutes = window.timer_minutes
            self.timer_seconds = window.timer_seconds
            self.update_timer_values()

    def update_team_names(self):
        self.label_team_one.setText(self.team_one_name)
        self.label_team_two.setText(self.team_two_name)

    def update_button_values(self, dialog):
        self.button_one_value = dialog.button_one_value
        self.button_two_value = dialog.button_two_value
        self.button_three_value = dialog.button_three_value

        self.pushButton_t1_b1.setText(str(self.button_one_value))
        self.pushButton_t2_b1.setText(str(self.button_one_value))
        self.pushButton_t1_b2.setText(str(self.button_two_value))
        self.pushButton_t2_b2.setText(str(self.button_two_value))
        self.pushButton_t1_b3.setText(str(self.button_three_value))
        self.pushButton_t2_b3.setText(str(self.button_three_value))

    def update_timer_values(self):
        self.label_timer.setText(f"{self.timer_minutes:02d}:{self.timer_seconds:02d}")

    def start_button_clicked(self):
        self.timer.start(1000)  # every 1 second
        self.update_countdown()

    def update_countdown(self):
        if self.timer_minutes == 0 and self.timer_seconds == 0:
            self.timer.stop()
            return
        if self.timer_seconds == 0:
            self.timer_seconds = 59
            self.timer_minutes -= 1
        else:
            self.timer_seconds -= 1
        self.update_timer_values()

    def stop_button_clicked(self):
        self.timer.stop()
        self.timer_minutes = 0
        self.timer_seconds = 0
        self.update_timer_values()

    def pause_button_clicked(self):
        if not self.paused:
            self.timer.stop()
            self.paused = True
        else:
            self.timer.start(1000)
            self.paused = False

    def reset_button_clicked(self):
        self.timer.stop()
        self.timer_minutes = self.default_minutes
        self.timer_seconds = self.default_seconds
        self.update_timer_values()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
