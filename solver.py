import sys
import puzz
import pdqpq
from searcher import Searcher

MAX_SEARCH_ITERS = 100000
GOAL_STATE = puzz.EightPuzzleBoard("012345678")


def solve_puzzle(start_state, strategy):
    """Perform a search to find a solution to a puzzle.
    
    Args:
        start_state: an EightPuzzleBoard object indicating the start state for the search
        flavor: a string indicating which type of search to run.  Can be one of the following:
            'bfs' - breadth-first search
            'ucost' - uniform-cost search
            'greedy-h1' - Greedy best-first search using a misplaced tile count heuristic
            'greedy-h2' - Greedy best-first search using a Manhattan distance heuristic
            'greedy-h3' - Greedy best-first search using a weighted Manhattan distance heuristic
            'astar-h1' - A* search using a misplaced tile count heuristic
            'astar-h2' - A* search using a Manhattan distance heuristic
            'astar-h3' - A* search using a weighted Manhattan distance heuristic
    
    Returns: 
        A dictionary containing describing the search performed, containing the following entries:
            'path' - a list of 2-tuples representing the path from the start state to the goal state 
                (both should be included), with each entry being a (str, EightPuzzleBoard) pair 
                indicating the move and resulting state for each action.  Omitted if the search 
                fails.
            'path_cost' - the total cost of the path, taking into account the costs associated 
                with each state transition.  Omitted if the search fails.
            'frontier_count' - the number of unique states added to the search frontier at any
                point during the search.
            'expanded_count' - the number of unique states removed from the frontier and expanded 
                (successors generated).
    """
    search_obj = Searcher(start_state, goal_state=GOAL_STATE)
    if strategy == 'bfs':
        return search_obj.BFS_solution()    
    elif strategy == 'ucost':
        return search_obj.UCS_solution()
    elif strategy == 'greedy-h1':
        return search_obj.Greedy_solution(h='h1')
    elif strategy == 'greedy-h2':
        return search_obj.Greedy_solution(h='h2')
    elif strategy == 'greedy-h3':
        return search_obj.Greedy_solution(h='h3')
    elif strategy == 'astar-h1':
        return search_obj.Astar_solution(h='h1')
    elif strategy == 'astar-h2':
        return search_obj.Astar_solution(h='h2')
    elif strategy == 'astar-h3':
        return search_obj.Astar_solution(h='h3')
    else:
        print("strategy not found")







def print_summary(results):
    if 'path' in results:
        print("found solution of length {}, cost {}".format(len(results['path']), 
                                                            results['path_cost']))
        for move, state in results['path']:
            # print("  {:5} {}".format(move, state))
            print(move)
            print(state.pretty())
            print()
    else:
        print("no solution found")
    print("{} states placed on frontier, {} states expanded".format(results['frontier_count'], 
                                                                    results['expanded_count']))


############################################

if __name__ == '__main__':

    start = puzz.EightPuzzleBoard(sys.argv[1])
    method = sys.argv[2]

    print("solving puzzle {} -> {}".format(start, GOAL_STATE))
    results = solve_puzzle(start, method)
    print_summary(results)
