from functools import partial
from random import randint
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

# def check():
#     if buttons[0][0].text() == "X" and buttons[0][1].text() == "X" and buttons[0][2].text() == "X" :
#         global msg_box
#         msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره یک برنده شد')
#         msg_box.show()
list=[]
def check():
    global buttons
    global msg_box
    #check rows
    for row in buttons:
        if row[0].text() == row[1].text() == row[2].text() =="X":
            msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره یک برنده شد')
            msg_box.show()
           

    #check columns
    for i in range(3):
        if buttons[0][i].text() == buttons[1][i].text() == buttons[2][i].text() == "X" :
                msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره یک برنده شد')
                msg_box.show()
               
    #check diagonals
        if buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text()=="X": 
            msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره یک برنده شد')
            msg_box.show()
           

        if buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text()=="X": 
            msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره یک برنده شد')
            msg_box.show()
            
  
        
    #check rows
    for row in buttons:
        if row[0].text() == row[1].text() == row[2].text() =="O":
            msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره دو برنده شد')
            msg_box.show()
           

    #check columns
    for i in range(3):
        if buttons[0][i].text() == buttons[1][i].text() == buttons[2][i].text() == "O" :
                msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره دو برنده شد')
                msg_box.show()
               

    #check diagonals
        if buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text()=="O": 
            msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره دو برنده شد')
            msg_box.show()
            

        if buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text()=="O": 
            msg_box = QMessageBox(windowTitle="تبریک", text='بازیکن شماره دو برنده شد')
            msg_box.show()
            

def play(row, col):
    global player
    if player == 1:
        if buttons[row][col].text() == "" :
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color : white; border-radius: 16px; border: 4px double rgba(200, 280, 200, 1);")
            cpu()
        else :
         global msg_box
         msg_box = QMessageBox(windowTitle="خطا", text="این خانه قبلا انتخاب شده است لطفا دوباره تلاش نمایید")
         msg_box.show()             
    check()  
    
def cpu():
        cell = buttons[randint(0, 2)][randint(0, 2)]
        global player
        if cell.text() == "":
            cell.setText("O")
            player = 1   
              
        else:
            return cpu()
    
        
app = QApplication([])
player = 1
loader = QUiLoader()
main = loader.load("main.ui")
main.show()

buttons = [[main.btn_1, main.btn_2, main.btn_3],
          [main.btn_4, main.btn_5, main.btn_6],
          [main.btn_7, main.btn_8, main.btn_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

def new_game():
    for i in range(3):
     for j in range(3):
        buttons[i][j].setText("")  
        buttons[i][j].setStyleSheet("background: rgba(72, 124, 200, 0.33); \
                    border-radius: 16px; border: 4px double rgba(200, 280, 200, 1); \
                    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); backdrop-filter: blur(8.8px); -webkit-backdrop-filter: blur(8.8px);")

main.new_game_btn.clicked.connect(new_game)
app.exec()
