from cProfile import label
from cgitb import text
from tkinter import *
import random


#A function to determine whose turn it is 
def NextTurn(row,column):
    global player
    if buttons[row][column]['text']=="" and CheckWinnner() is False:
        if player==players[0]:
            buttons[row][column]['text']=player
            if CheckWinnner() is False:
                player=players[1]
                label.config(text=(players[1]+" turn"))
            elif CheckWinnner() is True:
                label.config(text=(players[0]+" Won"))
            elif CheckWinnner() =='Tie':
                label.config(text=('Tie!'))
        else:
            buttons[row][column]['text']=player
            if CheckWinnner() is False:
                player=players[0]
                label.config(text=(players[0]+" turn"))
            elif CheckWinnner() is True:
                label.config(text=(players[1]+" Won"))
            elif CheckWinnner() =='Tie':
                label.config(text=('Tie!'))


#A function to determine the winner of the game                 
def CheckWinnner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text'] !="":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text'] !="":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif EmptySpaces() is False:
        for row in range(3):
            for coloums in range(3):
                buttons[row][coloums].config(bg="yellow")
        return 'Tie'
    else:
        return False


#A function to know how many places are left when playing
def EmptySpaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces-=1
    if spaces==0:
        return False
    else:
        return True


#A function to restart the game after the game ends
def NewGame():
    global player
    player=random.choice(players)
    label.config(text=(player+" turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")



window=Tk()
players=['X','O']
player=random.choice(players)
buttons=[
         [0,0,0],
         [0,0,0],
         [0,0,0]
         ]

label=Label(text=player + " turn",font=("consolas",40))
label.pack(side="top")
reset_button=Button(text="Restart",font=("consolas",20),command=NewGame)
reset_button.pack(side="top")
frame=Frame(window)
frame.pack()


for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font=("consolas",40),width=5,height=2,command=lambda row=row,column=column: NextTurn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.title("OX game")
icon = PhotoImage(file='pic.png')
window.iconphoto(True,icon)
window.mainloop()