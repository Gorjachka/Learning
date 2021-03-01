# player=1
# state=21
class GameStick:
    def __init__(self):
        self.player=1
        self.state=21
        # self.move=move

    def game(self):
        print('the number of sticks now:'+ self.state)
        while True:
            print('player'+ self.player)
            # while True:
            move=int(input('What is your move?'))
                # if move in [1,2,3] and move<state:
                #     break
                # print('Illegal move, try again')

            state=state-move
            print('the number of sticks now:'+ self.state)

            if state==1:
                print('player '+self.player+' wins!')
                break

            if player==1:
                player=2
            else:
                player=1

            print('Game over')
a= GameStick()
a.player=1
a.state=21
# player=1
# state=21
# print(f'the number of sticks now:{state}')
# while True:
#     print(f'player{player}')
#     # while True:
#     move=int(input('What is your move?'))
#         # if move in [1,2,3] and move<state:
#         #     break
#         # print('Illegal move, try again')
#
#     state=state-move
#     print(f'the number of sticks now:{state}')
#
#     if state==1:
#         print(f'player {player} wins!')
#         break
#
#     if player==1:
#         player=2
#     else:
#         player=1
#
# print('Game over')
