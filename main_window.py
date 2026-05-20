import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("design_1.ui",self)

        # --- initialise variables

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

    # ---- SLOTS ---- #
    def button_b1_clicked(self):
        print("hi")

    def button_b2_clicked(self):
        print("bonjour")

    def button_b3_clicked(self):
        print("hello young squire")

    def button_reset_score_clicked(self):
        print("hey you old bat")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
