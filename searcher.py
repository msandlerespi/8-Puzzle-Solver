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
        

    def _get_heuristic(self, state, type):
        """ Heuristic function
        
        Args:
            state: EightPuzzleBoard (the state that will get its heuristic calculated)
            type: "h1" | "h2" | "h3"
        Returns: 
            int (heuristic value)
        """
        pass
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
