from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget,QListWidgetItem, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox
app = QApplication([])
btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити").
box_time = QSpinBox()
box_time.setValue(30)
btn_ok = QPushButton("Відповісти")
question = QLabel("###")
#варіанти відповідей
RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()
rdbtn_1 = QRadioButton("answer1")
rdbtn_2 = QRadioButton("answer2")
rdbtn_3 = QRadioButton("answer3")
rdbtn_4 = QRadioButton("answer4")
RadioGroup.addButton(rdbtn_1)
RadioGroup.addButton(rdbtn_2)
RadioGroup.addButton(rdbtn_3)
RadioGroup.addButton(rdbtn_4)

#панелька з результатом
answerGroupBox = QGroupBox("результат тесту")
lb_result = QLabel("#")
lb_true_answer = QLabel("#")


#розміщення
ans1_layout = QHBoxLayout()
ans2_layout = QVBoxLayout()
ans3_layout = QVBoxLayout()

ans2_layout.addWidget(rdbtn_1)
ans2_layout.addWidget(rdbtn_2)


ans3_layout.addWidget(rdbtn_3)
ans3_layout.addWidget(rdbtn_4)

ans1_layout.addLayout(ans2_layout)
ans1_layout.addLayout(ans3_layout)












