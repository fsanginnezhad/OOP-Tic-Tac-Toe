from .color import Color


class Game(Color):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def draw_map(player1_moves: list[tuple], player2_moves: list[tuple]) -> None:
        """
        Draws the game board with the current moves made by the players.

        Args:
        player1_moves (list[tuple]): A list of tuples representing the moves made by player 1. # noqa E501
        player2_moves (list[tuple]): A list of tuples representing the moves made by player 2. # noqa E501

        Returns:
        None.
        """
        x = 1
        print(Color.color_blue(' _') * 3)
        for row in range(3):
            for col in range(3):
                if (row, col) in player1_moves:
                    print(
                        Color.color_blue('|') + Color.color_green('O'),
                        end=''
                    )
                elif (row, col) in player2_moves:
                    print(
                        Color.color_blue('|') + Color.color_red('X'),
                        end=''
                    )
                else:
                    print(
                        Color.color_blue('|') + Color.color_black(str(x)),
                        end=''
                    )
                x += 1
            print(Color.color_blue('|'))

    @staticmethod
    def check_win(moves: list[tuple]) -> bool:
        """
        Checks if a player has won the game based on their moves.

        Args:
        moves (list[tuple]): A list of tuples representing the moves made by a player. # noqa E501

        Returns:
        A bool indicating whether the player has won the game or not.
        """
        winner_moves = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for win_move in winner_moves:
            if all(move in moves for move in win_move):
                return True
        return False

    @staticmethod
    def conditions(o: str, x: str, *players: dict) -> str:
        """
        Determines the game outcome based on the players' states.

        Args:
        o (str): The symbol used by player 1.
        x (str): The symbol used by player 2.
        *players (dict): A variable number of dictionaries representing the state of each player. # noqa E501

        Returns:
        A string representing the game outcome, which could be one of the following: # noqa E501
        - "Player <o> Wins!" if the first player is winning, where <o> is the symbol used by player 1. # noqa E501
        - "Player <x> Wins!" if any other player is winning, where <x> is the symbol used by player 2. # noqa E501
        - "It's a tie!" if no player is winning.
        """
        for index, player in enumerate(players):
            if player['is_winning']:
                if index == 0:
                    return f'Player {Color.color_green(o)} Wins!'
                else:
                    return f'Player {Color.color_red(x)} Wins!'
        return "It's a tie!"
