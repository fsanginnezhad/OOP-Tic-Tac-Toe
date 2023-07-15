import random
from time import sleep
from game.models.game import Game
from game.models.color import Color
from game.helper.const import CELLS
from game.utils.funcs import clear_screen
from game.objects.players import (
    player1,
    player2
)


def main():
    """
    Plays a game of Tic Tac Toe between two players.

    This function starts a game between two players, represented by the 'player1' and 'player2' global dictionaries. # noqa E501
    The game alternates between each player, with 'O' representing the first player and 'X' representing the second. # noqa E501
    The function checks for a win or a tie after each move, and ends the game when one of these conditions is met. # noqa E501
    The function then prints the final game state, including the moves made by each player and the game outcome. # noqa E501

    Args:
    None.

    Returns:
    None.
    """
    o, x = 'O', 'X'
    while True:
        clear_screen()
        print(Color.color_blue_light('<<< Welcome to the game >>>'))
        Game.draw_map(player1.player['moves'], player2.player['moves'])
        player_move = Color.color_green(o)
        choice = input(f'\nEnter move Player {player_move}: ')
        if choice in CELLS:
            move = CELLS[choice]
            player1.player['moves'].append(move)
            CELLS.pop(choice)
        else:
            continue
        if Game.check_win(player1.player['moves']):
            player1.player['is_winning'] = True
            break
        if len(player1.player['moves']) + len(player2.player['moves']) == 9:
            break
        clear_screen()
        print(Color.color_blue_light('<<< Welcome to the game >>>'))
        Game.draw_map(player1.player['moves'], player2.player['moves'])
        print(f'\nPlaying Player {Color.color_red(x)} ...')
        sleep(2)
        choice = random.choice(list(CELLS.keys()))
        move = CELLS[choice]
        player2.player['moves'].append(move)
        CELLS.pop(choice)
        if Game.check_win(player2.player['moves']):
            player2.player['is_winning'] = True
            break
    clear_screen()
    Game.draw_map(player1.player['moves'], player2.player['moves'])
    print(Game.conditions(o, x, player1.player, player2.player))
