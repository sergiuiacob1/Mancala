import math
import random
from state import State, evaluateState
from transition import Transition, makeTransition
from game_config import numberOfHoles, turnAI, maxMiniMaxDepth


def getBestAIDecision(currentState: State):
    bestScore = minimax(currentState, maxMiniMaxDepth, True)
    print(f'Best score: {bestScore}')
    holes = [i for i in range(0, numberOfHoles)
             if currentState.stones[turnAI - 1][i] > 0]
    return random.choice(holes) + 1


def buildStateChildren(currentState: State):
    holes = [i for i in range(0, numberOfHoles)
             if currentState.stones[turnAI - 1][i] > 0]
    possibleStates = [makeTransition(
        currentState, Transition(hole)) for hole in holes]
    return possibleStates


def minimax(currentState: State, limit, maximixing):
    children = buildStateChildren(currentState)

    if maximixing:
        value = -math.inf
        for child in children:
            if limit == 1:
                childValue = evaluateState(currentState, child)
            else:
                childValue = minimax(child, limit - 1, False)
            value = max(value, childValue)
        return value
    else:
        value = math.inf
        for child in children:
            if limit == 1:
                childValue = evaluateState(currentState, child)
            else:
                childValue = minimax(child, limit - 1, True)
            value = min(value, childValue)        
        return value
