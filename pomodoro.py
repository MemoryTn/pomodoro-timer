# pomodoro.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLCDNumber, QTimer

class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 300, 200)

        self.lcd = QLCDNumber()
        self.label = QLabel("Press Start")
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 25 * 60  # 25 minutes

    def start_timer(self):
        self.timer.start(1000)
        self.label.setText("Working...")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.lcd.display(f"{minutes:02d}:{seconds:02d}")
        else:
            self.timer.stop()
            self.label.setText("Break time!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())
