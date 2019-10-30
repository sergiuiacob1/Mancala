from state import State
from transition import Transition, makeTransition
from game_config import numberOfHoles, turnAI
import random


def getBestAIDecision(currentState: State):
    holes = [i for i in range(0, numberOfHoles)
             if currentState.stones[turnAI - 1][i] > 0]
    possibleStates = [makeTransition(
        currentState, Transition(hole)) for hole in holes]
    return random.choice(holes) + 1
