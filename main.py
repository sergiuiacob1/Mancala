from state import State, getInitialState, displayState, getFinalScores
from transition import Transition, makeTransition
from game_config import numberOfHoles


def decisionIsIncorrect(state: State, hole):
    if state.turn == 1 and state.stones[0][hole - 1] == 0:
        return True
    if state.turn == 2 and state.stones[1][hole - 1] == 0:
        return True
    if hole <= 0 or hole > numberOfHoles:
        return True
    return False


if __name__ == '__main__':
    currentState = getInitialState()
    while currentState.isFinal() == False:
        displayState(currentState)
        # if (currentState.turn == 1):
        decision = int(input('Enter your decision: '))
        if decisionIsIncorrect(currentState, decision):
            print('Decision is incorrect, hole is empty!')
            continue
        transition = Transition(decision)
        currentState = makeTransition(currentState, transition)

    scores = getFinalScores(currentState)
    print(f'Game over. Scores: {scores}')
