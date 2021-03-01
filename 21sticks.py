# class DrNim:
#
#     def __init__(self,x):
#         self.x=x
#         self.marbles = list(range(1, 22))
#         self.player_marble, self.dr_nim_marble = 0, 0
#
#     def default_game(self):
#         """Run default game of Dr. Nim (impossible to win)."""
#         while len(self.marbles) > 0:
#                 player_marbles = self.x#int(input('yout number:'))
#                 if player_marbles <= 4:
#                     for i in range(player_marbles):
#                         self.player_marble = self.marbles.pop()
#                         self.win()
#                     print("Marbles left: {}\n".format(self.marbles))
#                     self.default_game_logic()
#
#     def default_game_logic(self):
#         """Run default game logic and calls self.win()."""
#         sub_marbles = 1
#
#         while len(self.marbles) % 4 != 0 and self.marbles != 0:
#             self.dr_nim_marble = self.marbles.pop()
#             sub_marbles += 1
#
#         print("Dr. Nim takes {} marble(s)".format(sub_marbles))
#         print("Marbles left: {}\n".format(self.marbles))
#
#         self.win()
#
#
#     def win(self):
#         """Check win conditions for game."""
#         if self.player_marble == 1:
#             print("You Won!")
#         elif self.player_2 == 1:
#             print("Player 2 Won!")
#         elif self.dr_nim_marble == 1:
#             print("Dr. Nim Won!")
#
#
#     def main():
#         """Create instance of DrNim()."""
#         game = DrNim(x)
#         game.two_players()
#
# if __name__ == "__main__":
#     main()


    #
    # class DrNim:
    #     """Dr. Nim is a mathematical game in which players 'release' marbles
    #     in turn. A player can only 'release' 1, 2, or 3 marbles. The player who
    #     'releases' the last marble wins!"""
    #
    #     def __init__(self):
    #         """Initialize class variables for game."""
    #         self.marbles = list(range(1, 22))
    #         self.player_marble, self.dr_nim_marble = 0, 0
    #
    #     def default_game(self):
    #         """Run default game of Dr. Nim (impossible to win)."""
    #         while len(self.marbles) > 0:
    #             try:
    #                 player_marbles = int(input("Marbles to release [1, 2, 3]: "))
    #             except ValueError:
    #                 print("ERROR: Input not an integer!")
    #             else:
    #                 if player_marbles <= 4:
    #                     for i in range(player_marbles):
    #                         self.player_marble = self.marbles.pop()
    #                         self.win()
    #                     print("Marbles left: {}\n".format(self.marbles))
    #                     self.default_game_logic()
    #                 else:
    #                     print("ERROR: Only allowed number < 4!\n")
    #
    #     def default_game_logic(self):
    #         """Run default game logic and calls self.win()."""
    #         sub_marbles = 1
    #
    #         while len(self.marbles) % 4 != 0 and self.marbles != 0:
    #             self.dr_nim_marble = self.marbles.pop()
    #             sub_marbles += 1
    #
    #         print("Dr. Nim takes {} marble(s)".format(sub_marbles))
    #         print("Marbles left: {}\n".format(self.marbles))
    #
    #         self.win()
    #
    #     def win(self):
    #         """Check win conditions for game."""
    #         if self.player_marble == 1:
    #             print("You Won!")
    #         elif self.dr_nim_marble == 1:
    #             print("Dr. Nim Won!")
    #
    #
    # def main():
    #     """Create instance of DrNim()."""
    #     game = DrNim()
    #     game.default_game()
    #
    #
    # if __name__ == "__main__":
    #     main()