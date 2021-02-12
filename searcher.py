from pdqpq import PriorityQueue
from puzz import EightPuzzleBoard

class Searcher():
    def __init__(self, start_state, goal_state = EightPuzzleBoard("012345678")):
        self.start_state = start_state
        self.goal_state = goal_state
        self.frontier = PriorityQueue()
        self.explored = {}
    def _expand(self, state):
        """ Expand method

        Args:
            state: EightPuzzleBoard (state being expanded)
        Returns: 
            list (list of neighboring states)
        """
        pass
    def _get_heuristic(self, state, type):
        """ Heuristic function
        
        Args:
            state: EightPuzzleBoard (the state that will get its heuristic calculated)
            type: "h1" | "h2" | "h3"
        Returns: 
            int (heuristic value) | None (if type is invalid)
        """
        assert type == "h1" or type == "h2" or type == "h3", "Invalid Heuristic Type"
        heuristic = 0
        if type == "h1":
        #h1 = # of misplaced tiles
            for i in range(10):
            # Goes through 0-9 and compares the position of that number on the state arg vs the goal state (if it doesnt match, then the heuristic value increments by 1)
                if self.goal_state.find(i) != state.find(i):
                    heuristic += 1
        elif type == "h2":
        #h2 = the sum of the distances of the tiles from their goal positions
            for i in range (10):
            # Goes through 0-9 and subtracts the coordinates of the state arg with the coordinates of the goal state (then adds the difference to the heuristic value) 
                goal_coor = self.goal_state.find(i)
                state_coor = state.find(i)
                heuristic += abs(state_coor[0] - goal_coor[0]) + abs(state_coor[1] - goal_coor[1])
        else:
        #h3 = modified version of h2 (takes into account transition costs)
            for i in range (10):
            # Same has h2, but multiplies the difference by i^2 before adding it to the heuristic value
                goal_coor = self.goal_state.find(i)
                state_coor = state.find(i)
                heuristic += i * i * (abs(state_coor[0] - goal_coor[0]) + abs(state_coor[1] - goal_coor[1]))
        return heuristic
    def _get_weight(self, state):
        """ Weight function

        Args:
            state: EightPuzzleBoard (the state that will get its weight calculated) 
        Returns:
            int (weight value)
        """
        pass
    def BFS_solution(self):
        """ Solution method

        Returns 
            results = {
                'path': [],
                'path_cost': 0,
                'frontier_count': 0,
                'expanded_count': 0,
                }
        """
        pass
    def UCS_solution(self):
        """ Solution method

        Returns 
            results = {
                'path': [],
                'path_cost': 0,
                'frontier_count': 0,
                'expanded_count': 0,
                }
        """
        pass
    def Greedy_solution(self):
        """ Solution method

        Returns 
            results = {
                'path': [],
                'path_cost': 0,
                'frontier_count': 0,
                'expanded_count': 0,
                }
        """
        pass
    def Astar_solution(self):
        """ Solution method

        Returns 
            results = {
                'path': [],
                'path_cost': 0,
                'frontier_count': 0,
                'expanded_count': 0,
                }
        """
        pass
