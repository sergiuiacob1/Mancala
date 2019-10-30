from game_config import *


class State:
    """
    `State.stones` is a matrix; `stones[i]` is an array with the stones for the `i`th player
    For example, if stones[0] = [3, 4, 4, 5, 0], then the first hole has 3 stones, the second hole has 4 stones and so on
    `State.mancalas` is an array; `mancalas[i]` represents how many stones are in player's `i` mancala
    `State.turn` signifies whose player's turn it is
    """

    def __init__(self, stones, mancalas, turn):
        self.stones = stones
        self.mancalas = mancalas
        self.turn = turn

    def __eq__(self, other, turn):
        return self.stones == other.stones and self.mancalas == other.mancalas and self.turn == other.turn

    def isFinal():
        """
        The game is over when one side has no more stones left to move
        """
        return all([x == 0 for x in self.stones[0]]) or all([x == 0 for x in self.stones[1]])


def getInitialState():
    stones1 = [initialNumberOfStones for _ in range(0, numberOfHoles)]
    stones2 = [initialNumberOfStones for _ in range(0, numberOfHoles)]
    mancalas = [0, 0]
    return State([stones1, stones2], mancalas, 1)


def getFinalScores(state: State):
    return [state.mancalas[0] + sum(state.stones[0]), state.mancalas[1] + sum(state.stones[1])]


def displayState(state: State):
    """
    Player 1 will be down, Player 2 will be up
    """
    mancalaFormat = '{:10s}'
    stoneFormat = '{:5s}'

    print(mancalaFormat.format(''), end='')
    for i in range(0, len(state.stones[1])):
        print(stoneFormat.format(str(state.stones[1][i])), end='')
    print('{0: ^10}'.format(str(state.mancalas[1])))

    print(mancalaFormat.format(str(state.mancalas[0])), end='')
    for i in range(0, len(state.stones[0])):
        print(stoneFormat.format(str(state.stones[0][i])), end='')
    print('')


def evaluateState(state: State):
    """
    Evaluates... what?
    """
    ...
