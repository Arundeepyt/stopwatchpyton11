import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget
)
from PyQt5.QtCore import QTimer, Qt

class NeonStopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.ms = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Neon Stopwatch")
        self.setFixedSize(400, 500)

        # Time Display
        self.time_label = QLabel("00:00:00.000")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            QLabel {
                font-size: 36px;
                color: #00ffff;
                background: #000000;
                border: 3px solid #00ffff;
                border-radius: 10px;
                padding: 20px;
            }
        """)

        # Buttons
        self.start_btn = QPushButton("▶ Start")
        self.stop_btn = QPushButton("⏸ Stop")
        self.reset_btn = QPushButton("⟲ Reset")
        self.lap_btn = QPushButton("★ Lap")

        for btn in [self.start_btn, self.stop_btn, self.reset_btn, self.lap_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: black;
                    color: #00ffff;
                    font-size: 16px;
                    border: 2px solid #00ffff;
                    border-radius: 10px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #00ffff;
                    color: black;
                }
            """)

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)
        self.lap_btn.clicked.connect(self.lap)

        # Lap list
        self.lap_list = QListWidget()
        self.lap_list.setStyleSheet("""
            QListWidget {
                background-color: black;
                color: #00ffff;
                border: 2px solid #00ffff;
                font-size: 14px;
            }
        """)

        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.stop_btn)
        hbox.addWidget(self.reset_btn)
        hbox.addWidget(self.lap_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lap_list)

        self.setLayout(vbox)

        self.setStyleSheet("background-color: #050505;")

    def start(self):
        self.timer.start(10)  # update every 10ms

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.ms = 0
        self.time_label.setText("00:00:00.000")
        self.lap_list.clear()

    def lap(self):
        self.lap_list.addItem(self.time_label.text())

    def update_time(self):
        self.ms += 10

        hours = self.ms // 3600000
        minutes = (self.ms % 3600000) // 60000
        seconds = (self.ms % 60000) // 1000
        millis = self.ms % 1000

        self.time_label.setText(
            f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NeonStopwatch()
    window.show()
    sys.exit(app.exec_())
