import puissance_4 as ps

if __name__ == "__main__":
    game = ps.Game()
    column = int(input(f'{game.player} plays: '))
    while game.game_run(column):
        column = int(input(f'{game.player} plays: '))
    print('The winner is: ',game.player)
