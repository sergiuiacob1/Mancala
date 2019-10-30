from state import State, getInitialState, displayState, getFinalScores
from transition import Transition, makeTransition
from game_config import numberOfHoles, turnHuman
from ai import getBestAIDecision


def decisionIsIncorrect(state: State, hole):
    if state.stones[state.turn - 1][hole - 1] == 0:
        return True
    if hole <= 0 or hole > numberOfHoles:
        return True
    return False


if __name__ == '__main__':
    currentState = getInitialState()
    while currentState.isFinal() == False:
        displayState(currentState)
        if currentState.turn == turnHuman:
            decision = int(input('Enter your decision: '))
        else:
            decision = getBestAIDecision(currentState)
            print(f'AI took decision {decision}')
        if decisionIsIncorrect(currentState, decision):
            print('Decision is incorrect, hole is empty!')
            continue
        transition = Transition(decision)
        currentState = makeTransition(currentState, transition)
        print('')

    print ('Final state:')
    displayState(currentState)
    scores = getFinalScores(currentState)
    print(f'Game over. Scores: {scores}')
