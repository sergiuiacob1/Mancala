from state import State


def displayState(state: State):
    mancalaFormat = '{:10s}'
    stoneFormat = '{:5s}'
    print(mancalaFormat.format(str(state.mancalas[0])), end='')
    for i in range(0, len(state.stones[0])):
        print(stoneFormat.format(str(state.stones[0][i])), end='')
    print('')

    print(mancalaFormat.format(''), end='')
    for i in range(0, len(state.stones[1])):
        print(stoneFormat.format(str(state.stones[1][i])), end='')
    print('{0: ^10}'.format(str(state.mancalas[1]))) 
