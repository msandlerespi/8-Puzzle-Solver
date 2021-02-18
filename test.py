from puzz import EightPuzzleBoard
import solver
import random

#random input generator for testing 
def get_input(num):
    state = solver.GOAL_STATE
    path = [state]
    for i in range(num):
        successes = list(state.successors().values())
        success_state = random.choice(successes)
        state = success_state
    print(state)

get_input(1000)