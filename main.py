from state import getInitialState, displayState, getFinalScores
from game_config import numberOfHoles

if __name__ == '__main__':
    currentState = getInitialState()
    while currentState.isFinal() == False:
        displayState(currentState)
        if (currentState.turn == 1):
            decision = int(input('Enter your decision...'))
            if decisionIsIncorrect(currentState, decision):
                print('Decision is incorrect, hole is empty!')
                continue

    scores = getFinalScores(currentState)
    print(f'Game over. Scores: {scores})


def decisionIsIncorrect(state: State, hole)
   if state.turn == 1 and state.stones[0][hole] == 0:
        return True
    if state.turn == 2 and state.stones[1][hole] == 0:
        return True
    if hole <= 0 or hole > numberOfHoles:
        return True
    return False
