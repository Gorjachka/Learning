'''
This is the a game '21 sticks'.(Nim)

In this version of game are 21 sticks and the groups are made up of 3.
The game is played by each player selecting sticks to remove from the groups until there are no stickss left.
(when 3 sticks left to one player).
The rules are that players take turns in removing objects.
Players may remove as many objects as they want each turn, but can only remove objects from one group each turn.
The player who is taken the last sticks is the winer.

This game has been programed into Python 3 using Tkinter .
'''

import tkinter
from tkinter import *


root = tkinter.Tk()
root.geometry("600x200+300+300")
root.resizable(0,0)
root.title("21sticks")


player_label_data=StringVar()
Label(
    root,
    font='none 16 bold',
    textvariable = player_label_data
).pack()
player_label_data.set(' player 1 turn')


sticks_label_data=StringVar()
Label(
    root,
    font='none 16 bold',
    textvariable = sticks_label_data
).pack()
sticks_label_data.set('  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  ')


kind_of_stick='  /  '
player = 1
sticks = 21


def Players_turn():
    """ define  players turn to make move """
    global player
    global sticks
    if player == 1:
        player = 2
    else:
        player = 1
    return


def Game(move,player):
    """ Run game and insert data into labels """
    global sticks
    while sticks > 3:
        player_label_data.set( f'now player {player} turn')
        sticks = sticks - move
        data.set(f'the number of sticks now: {sticks}')
        sticks_label_data.set(kind_of_stick*sticks)
        if sticks <= 3:
            data.set(f'player {player} wins!')
        break


def btn_1_click():
    """ Run botton 1 logic while cklicked """
    move = 1
    Players_turn()
    Game(move,player)
    return move,player

def btn_2_click():
    """ Run botton 2 logic while cklicked """
    move = 2
    Players_turn()
    Game(move, player)
    return move, player

def btn_3_click():
    """ Run botton 3 logic while cklicked """
    move = 3
    Players_turn()
    Game(move, player)
    return move, player


data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = CENTER,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
    height=2
)


lbl.pack(expand = True, fill = "both")
data.set(f"Let's play!  The number of sticks: 21")

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_click,
    fg="blue"
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_click,
    fg='red'
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_click,
    fg='green'
)
btn3.pack(side = LEFT, expand = True, fill = "both",)


root.mainloop()