import math
import random
from state import State, evaluateState
from transition import Transition, makeTransition, isTransitionValid
from game_config import numberOfHoles, turnAI, maxMiniMaxDepth


def getBestAIDecision(currentState: State):
    scores = []
    children, transitions = buildStateChildren(currentState)
    for child in children:
        scores.append(minimax(child, maxMiniMaxDepth, True))
    maxScoreIndex = scores.index(max(scores))
    return transitions[maxScoreIndex].hole + 1


def buildStateChildren(currentState: State):
    transitions = [Transition(i) for i in range(0, numberOfHoles)
                   if isTransitionValid(currentState, Transition(i))]
    possibleStates = [makeTransition(
        currentState, transition) for transition in transitions]
    return possibleStates, transitions


def minimax(currentState: State, limit, maximixing):
    children, _ = buildStateChildren(currentState)

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
