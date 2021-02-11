from pdqpq import PriorityQueue
from puzz import EightPuzzleBoard

class Searcher():
    def __init__(self, start_state, goal_state = EightPuzzleBoard("012345678")):
        self.start_state = start_state
        self.goal_state = goal_state
        self.frontier = PriorityQueue()
        self.explored = {}
    def expand(self, state):
        """ expand method
        state: state being expanded (EightPuzzleBoard) 
        return: list of neighboring states (list)
        """
        pass
    def get_heuristic(self, state, type):
        """ heuristic function
        state: the state that will get its heuristic calculated (EightPuzzleBoard)
        type: "h1" | "h2" | "h3"
        return: heuristic value (int)
        """
        pass
    def get_weight(self, state):
        """ weight function
        state: the state that will get its weight calculated (EightPuzzleBoard)
        return: weight value (int)
        """
        pass
    def findSolution(self):
        pass

class BFS(Searcher):
    pass
class UCS(Searcher):
    pass
class Greedy(Searcher):
    pass
class Astar(Searcher):
    pass
