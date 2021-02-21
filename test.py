from puzz import EightPuzzleBoard
import solver
from searcher import Searcher
import random

#random input generator for testing 
def get_input(num):
    state = solver.GOAL_STATE
    path = [state]
    for i in range(num):
        successes = list(state.successors().values())
        success_state = random.choice(successes)
        state = success_state
    return state

# print(get_input(1000))

def test_heuristic():
    searcher = Searcher(get_input(50))
    test_state = EightPuzzleBoard("014325678")
    print(searcher._get_heuristic(test_state, "h2"))

# test_heuristic()

def test_cost():
    searcher = Searcher(get_input(50))
    test_state1 = EightPuzzleBoard("6013485")
    test_state2 = EightPuzzleBoard("012345678")
    print(searcher._get_cost(test_state1, test_state2))

test_cost()