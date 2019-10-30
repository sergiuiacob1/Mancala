from state import State
from game_config import numberOfHoles


def Transition:
    def __init__(self, hole):
        self.hole = hole


def makeTransition(state: State, transition: Transition):
    """
    Transitions from `state` to a `newState` by moving the stones from `transition.hole`
    This function assumes that `transition` can be made upon `state`
    """
    newStones1 = list(state.stones[0])
    newStones2 = list(state.stones[1])
    newMancalas = list(state.mancalas)
    stonesToMove = state.stones[state.turn - 1]
    newTurn = state.turn % 2 + 1

    if state.turn == 1:
        # Player 1 is moving
        newStones1[transition.hole] = 0

        # Initially, I start from transition.hole on my board
        i = transition.hole
        while stonesToMove > 0:
            # Put on player 1's board
            while i < numberOfHoles and stonesToMove > 0:
                newStones1[i] += 1
                stonesToMove -= 1
                i += 1

            # put on player 1's mancala
            if stonesToMove > 0:
                newMancalas[0] += 1
                stonesToMove -= 1
                if stonesToMove == 0:
                    # If, when placing the last stone, I place it in my Mancala, I take another turn
                    # so turn for the new state will be 1
                    newTurn = 1
                    break
            elif stonesToMove == 0:
                # If, when placing the last stone, I place it on my board, I capture the stones from the opposite side
                newStones1[i - 1] += newStones2[i - 1]
                newStones2[i - 1] = 0

            # put on player 2's board
            i = numberOfHoles - 1
            while i >= 0 and stonesToMove > 0:
                newStones2[i] += 1
                stonesToMove -= 1
                i -= 1

            # I have to go counter-clock wise, so I'm starting with the position 0 on Player 1's board
            i = 0
    else:
        # Player 2 is moving
        newStones2[transition.hole] = 0

        # Initially, I start from transition.hole on my board
        i = transition.hole
        while stonesToMove > 0:
            # Put on player 2's board
            while i >= 0 and stonesToMove > 0:
                newStones2[i] += 1
                stonesToMove -= 1
                i -= 1

            # put on player 2's mancala
            if stonesToMove > 0:
                newMancalas[1] += 1
                stonesToMove -= 1
                if stonesToMove == 0:
                    # If, when placing the last stone, I place it in my Mancala, I take another turn
                    # so turn for the new state will be 2
                    newTurn = 2
                    break
            elif stonesToMove == 0:
                # If, when placing the last stone, I place it on my board, I capture the stones from the opposite side
                newStones2[i - 1] += newStones1[i - 1]
                newStones1[i - 1] = 0

            # put on player 1's board
            i = 0
            while i < numberOfHoles and stonesToMove > 0:
                newStones1[i] += 1
                stonesToMove -= 1
                i += 1

            # I have to go counter-clock wise, so I'm starting with the last position on Player 2's board
            i = numberOfHoles - 1

    newState = State([newStones1, newStones2], newMancalas, newTurn)