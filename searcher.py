from pdqpq import PriorityQueue
from puzz import EightPuzzleBoard

class Searcher():
    def __init__(self, start_state, goal_state = EightPuzzleBoard("012345678")):
        self.start_state = start_state
        self.goal_state = goal_state
        self.frontier = PriorityQueue()
        self.frontier_count = 0
        self.explored_set = set()
        # dictionary mapping a parent state to a tuple of the form: (str: move that it took to get to the key, EightPuzzleBoard: the state before it)
        # {parent_state: ("up | down | left | right", child_state)}
        self.predecessor_dict = {} 
    def _get_heuristic(self, state, h):
        """ Heuristic function
        
        Args:
            state: EightPuzzleBoard (the state that will get its heuristic calculated)
            h: "h1" | "h2" | "h3"
        Returns: 
            int (heuristic value) | None (if h is invalid)
        """
        assert h == "h1" or h == "h2" or h == "h3", "Invalid Heuristic h"
        heuristic = 0
        if h == "h1":
        #h1 = # of misplaced tiles
            for i in range(10):
            # Goes through 0-9 and compares the position of that number on the state arg vs the goal state (if it doesnt match, then the heuristic value increments by 1)
                if self.goal_state.find(i) != state.find(i):
                    heuristic += 1
        elif h == "h2":
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
    def _get_cost(self, predecessor, successor):
        """ Cost function -> calculates cost between a predeccessor and its successor

        Args:
            state: EightPuzzleBoard (the state that will get its weight calculated) 
        Returns:
            int (weight value)
        """
        coors = predecessor.find("0") # (x ,y)
        tile_moved = int(successor._get_tile(coors[0], coors[1]))
        return tile_moved * tile_moved
    def _get_result(self):
        """ Path function 
        Returns:
           {
            'path': [],
            'path_cost': 0,
            'frontier_count': 0,
            'expanded_count': 0,
           }
        """
        path = []
        path_cost = 0
        cur_node = self.goal_state
        while cur_node != self.start_state: 
            predecessor_info = self.predecessor_dict.get(cur_node) # tuple(str of the move that it took to get to cur_node, EightPuzzleBoard of the state that came before it)
            previous_node = (predecessor_info[0], cur_node) 
            path.append(previous_node) # tuple(str of the move that it took to get to cur_node, cur_node)
            path_cost += self._get_cost(predecessor_info[1], cur_node)
            cur_node = predecessor_info[1]
        path_cost += self._get_cost(self.predecessor_dict.get(cur_node)[1], cur_node) 
        path.append(("", cur_node))
        path.reverse()
        return {
            'path': path,
            'path_cost': path_cost,
            'frontier_count': self.frontier_count,
            'expanded_count': len(self.explored_set),
           }
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
        priority_num = 0
        self.frontier.add(self.start_state, priority=priority_num)
        self.frontier_count += 1

        while len(self.frontier) != 0:
            state = self.frontier.pop()
            self.explored_set.add(state)
            for successor in state.successors().items():
            # successor is tuple in the form (move: str, successor: EightBoardPuzzle)
                if (successor[1] not in self.frontier) and (successor[1] not in self.explored_set):
                    if successor[1] == self.goal_state:
                        self.predecessor_dict[successor[1]] = (successor[0], state)
                        return self._get_result()
                    else:
                        priority_num += 1
                        self.frontier.add(successor[1], priority=priority_num)
                        self.predecessor_dict[successor[1]] = (successor[0], state)
                        self.frontier_count += 1
        return {'frontier_count' : self.frontier_count, 'expanded_count' : len(self.explored_set)}
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
        
    def Greedy_solution(self, h):
        """ Solution method
        
        Args
            h = 'h1' | 'h2' | 'h3'
        Returns 
            results = {
                'path': [],
                'path_cost': 0,
                'frontier_count': 0,
                'expanded_count': 0,
                }
        """
        self.frontier.add(self.start_state, priority=0)
        self.frontier_count += 1

        while len(self.frontier) != 0:
            state = self.frontier.pop()
            self.explored_set.add(state)
            for successor in state.successors().items():
            # successor is tuple in the form (move: str, successor: EightBoardPuzzle)
                if (successor[1] not in self.explored_set):
                    if successor[1] == self.goal_state:
                        self.predecessor_dict[successor[1]] = (successor[0], state)
                        return self._get_result()
                    else:
                        self.frontier.add(successor[1], priority=self._get_heuristic(successor[1], h))
                        self.predecessor_dict[successor[1]] = (successor[0], state)
                        self.frontier_count += 1
        return {'frontier_count' : self.frontier_count, 'expanded_count' : len(self.explored_set)}
    def Astar_solution(self, h):
        """ Solution method
         
        Args
            h = 'h1' | 'h2' | 'h3'
        Returns 
            results = {
                'path': [],
                'path_cost': 0,
                'frontier_count': 0,
                'expanded_count': 0,
                }
        """
        pass