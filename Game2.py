# # import DrNim
# import tkinter
# from tkinter import *
# root = tkinter.Tk()
# root.geometry("600x200+300+300")
# root.resizable(0,0)
# root.title("21sticks")
# l=Label(root, text=f'turn player', font='none 16 bold').pack()
#
# #
# # def Game(x):
# #
# #     global state
# #     global player
# #
# #
# #     while True:
# #         data.set(f'player{player}')
# #         move = x  # or  btn_2_isclicked() or btn_3_isclicked
# #         state = state - move
# #         data.set(f'the number of sticks now: {state}')
# #
# #
# #         if state <= 1:
# #             data.set(f'player {player} wins!')
# #         break
# #
# #         if player == 1:
# #                 player = 2
# #         else:
# #                 player = 1
# #         data.set('Game is over')
# # class DrNim:
# #         """Dr. Nim is a mathematical game in which players 'release' marbles
# #         in turn. A player can only 'release' 1, 2, or 3 marbles. The player who
# #         'releases' the last marble wins!"""
#
#         # def __init__(self,x):
#         #     """Initialize class variables for game."""
#         #     self.x=x
#         #     self.marbles = list(range(1, 22))
#         #     self.player_marble, self.dr_nim_marble = 0, 0
#         #
#         # def default_game(self):
#         #     """Run default game of Dr. Nim (impossible to win)."""
#         #     while len(marbles) > 0:
#         #         try:
#         #             player_marbles = x#int(input("Marbles to release [1, 2, 3]: "))
#         #         except ValueError:
#         #             print("ERROR: Input not an integer!")
#         #         else:
#         #             if player_marbles <= 4:
#         #                 for i in range(player_marbles):
#         #                     player_marble = marbles.pop()
#         #                     self.win()
#         #                 data.set("Marbles left: {}\n".format(self.marbles))
#         #                 self.default_game_logic()
#         #             else:
#         #                 print("ERROR: Only allowed number < 4!\n")
#         #
#         # def default_game_logic(self):
#         #     """Run default game logic and calls self.win()."""
#         #     sub_marbles = 1
#         #
#         #     while len(self.marbles) % 4 != 0 and self.marbles != 0:
#         #         self.dr_nim_marble = self.marbles.pop()
#         #         sub_marbles += 1
#         #
#         #     data.set("Dr. Nim takes {} marble(s)".format(sub_marbles))
#         #     data.set("Marbles left: {}\n".format(self.marbles))
#         #
#         #     self.win()
#         #
#         # def win(self):
#         #     """Check win conditions for game."""
#         #     if self.player_marble == 1:
#         #         data.set("You Won!")
#         #     elif self.dr_nim_marble == 1:
#         #         data.set("Dr. Nim Won!")
#         #
#         #
#         # def main():
#         #     """Create instance of DrNim()."""
#         #     game = DrNim()
#         #     game.default_game()
#         #
#         #
#         # # if __name__ == "__main__":
#         # #     main()
# sticks = int(13)
#
# playerState = int(0)
#
# # game mechanics
#
# def game(x):
#     global sticks
#     global playerState
#     while (sticks > 0):
#         if (playerState % 2 != 1):
#             playerMove = (f'Player One, please enter your move:{x}')
#             if (playerMove > 0) and (playerMove < 5) and (playerMove <= sticks):
#                 sticks = sticks - playerMove
#                 playerState += 1
#                 data.set
#                 sticks
#                 data.set
#                 playerState
#             else:
#                 data.set
#                 "Illegal move.  Try again."
#         else:
#             playerMove = (f'Player One, please enter your move:{x}')
#             if (playerMove > 0) and (playerMove < 5) and (playerMove <= sticks):
#                 sticks = sticks - playerMove
#                 playerState += 1
#                 data.set
#                 sticks
#                 data.set
#                 playerState
#
#     winner = int(playerState % 2)
#
#     if (winner != 1):
#         data.set
#         "Congratulations player 1"
#     else:
#         data.set
#         "Congratulations player 2"
# # function for numerical button clicked
#
# def btn_1_isclicked():
#
#     x=1
#     game(x)
#     return int(x)
#
# def btn_2_isclicked():
#     x = 2
#     # game.default_game(x)
#     game(x)
#     return x
#
#
# def btn_3_isclicked():
#     x = 3
#     # game.default_game(x)
#     game(x)
#     return x
#
#
# # # the label that shows the result
# data = StringVar()
# lbl = Label(
#     root,
#     text = "Label",
#     anchor = CENTER,
#     font = ("Verdana", 20),
#     textvariable = data,
#     background = "#ffffff",
#     fg = "#000000",
#     height=3
#
#  )
# lbl.pack(expand = True, fill = "both")
# data.set(f'Let"s play: the number of sticks now:21')
# #
# # the frames section
# btnrow1 = Frame(root)
# btnrow1.pack(expand = True, fill = "both")
#
# btnrow2 = Frame(root)
# btnrow2.pack(expand = True, fill = "both")
#
# btnrow3 = Frame(root)
# btnrow3.pack(expand = True, fill = "both")
#
# btnrow4 = Frame(root)
# btnrow4.pack(expand = True, fill = "both")
#
# #
# # # The buttons section
# btn1 = Button(
#     btnrow1,
#     text = "1",
#     font = ("Verdana", 22),
#     relief = GROOVE,
#     border = 0,
#     command = btn_1_isclicked,
#     fg="blue"
# )
# btn1.pack(side = LEFT, expand = True, fill = "both",)
#
# btn2 = Button(
#     btnrow1,
#     text = "2",
#     font = ("Verdana", 22),
#     relief = GROOVE,
#     border = 0,
#     command = btn_2_isclicked,
# )
# btn2.pack(side = LEFT, expand = True, fill = "both",)
# #
# btn3 = Button(
#     btnrow1,
#     text = "3",
#     font = ("Verdana", 22),
#     relief = GROOVE,
#     border = 0,
#     command = btn_3_isclicked,
# )
# btn3.pack(side = LEFT, expand = True, fill = "both",)
#
#
# root.mainloop()

# Nim program prototype

# variables for the game.

sticks = int(13)

playerState = int(0)

# game mechanics


while (sticks > 0):
    if (playerState % 2 != 1):
        playerMove = int(input("Player One, please enter your move:"))
        if (playerMove > 0) and (playerMove < 5) #and (playerMove <= sticks):
            sticks = sticks - playerMove
            playerState += 1
            print (sticks)
            print (playerState)
        else:
            print
            "Illegal move.  Try again."
    else:
        playerMove = int(input("Player Two, please enter your move:"))
        if (playerMove > 0) and (playerMove < 5) and (playerMove <= sticks):
            sticks = sticks - playerMove
            playerState += 1
            print(sticks)
            print(playerState)

winner = int(playerState % 2)

if (winner != 1):
    print
    "Congratulations player 1"
else:
    print
    "Congratulations player 2"