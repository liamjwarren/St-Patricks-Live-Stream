#! python3
# Copyright
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel


class AppBase(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setMinimumSize(200, 200)
        self.setWindowTitle("St. Patrick's Live Stream")
        self.initLabels()
        self.initButtons()
        self.initView()

    def initLabels(self):
        self.altar_label = QLabel("Altar Presets")
        self.other_label = QLabel("Other Presets")
        self.live_label = QLabel("Live Camera View")

    def initButtons(self):
        self.entire_altar_button = QPushButton("Entire Altar")
        self.pulpit_button = QPushButton("Pulpit")
        self.altar_button = QPushButton("Altar")
        self.cantor_button = QPushButton("Cantor")
        self.priest_chair_button = QPushButton("Priest's Chair")
        self.priest_center = QPushButton("Priest")

        self.other_label = QLabel("Other Presets")
        self.baptism_button = QPushButton("Baptism Font")
        self.organ_button = QPushButton("View of Organ")
        self.risen_christ_button = QPushButton("Risen Christ Statue")

    def initView(self):
        self.photo = QLabel()

        # This is a temporary placeholder for now.
        self.photo.setPixmap(QPixmap('PXL_20201127_151314000.jpg'))
        self.photo.setScaledContents(True)
        self.layout()

    def layout(self):
        self.altar_layout = QVBoxLayout()
        self.altar_layout.addWidget(self.altar_label, Qt.AlignTop)
        self.altar_layout.addWidget(self.entire_altar_button)
        self.altar_layout.addWidget(self.priest_chair_button)
        self.altar_layout.addWidget(self.altar_button)
        self.altar_layout.addWidget(self.priest_center)
        self.altar_layout.addWidget(self.cantor_button)

        self.general_layout = QVBoxLayout()
        self.general_layout.addWidget(self.other_label, Qt.AlignTop)
        self.general_layout.addWidget(self.baptism_button)
        self.general_layout.addWidget(self.organ_button)
        self.general_layout.addWidget(self.risen_christ_button)

        self.video_layout = QVBoxLayout()
        self.video_layout.addWidget(self.photo)


        self.layout = QHBoxLayout()
        self.layout.addLayout(self.altar_layout)
        self.layout.addLayout(self.general_layout)
        self.layout.addLayout(self.video_layout)

        self.setLayout(self.layout)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = AppBase()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()