from Algorithms.BFS import bfs
from Algorithms.DFS import dfs
from Algorithms.UCS import ucs
from Algorithms.AStar import aStar
from Algorithms.Greedy import greedy
from Calc.calcCosts import *

# Dictionary
# DicKeys    : str
# DicValues  : list of strs
# Usage      : BFS , DFS
graphWithoutCost = {
    'S': ['D', 'A', 'B'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G', 'D'],
    'D': ['G'],
}

# Dictionary
# DicKeys    : str
# DicValues  : list of tuples(node,costToNode)
# Usage      : UCS , AStar , Greedy
graphWithCost = {
    'S': [('A', 1), ('B', 4),],
    'A': [('B', 2), ('C', 5),('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
}

searchingUsingBFS = bfs(graphWithoutCost, 'S', 'G')
searchingUsingDFS = dfs(graphWithoutCost, 'S', 'G')
searchingUsingUCS = ucs(graphWithCost, 'S', 'G');           pathCost = pathCost(searchingUsingUCS)
searchingUsingASTAR = aStar(graphWithCost, 'S', 'G');       pathCostWithHeuristic = pathCostWithHeuristic(searchingUsingASTAR)[0]
searchingUsingGreedy = greedy(graphWithCost, 'S', 'G');     heuristicCost = heuristicCost(searchingUsingGreedy)[0]

print("BFS solution is ", searchingUsingBFS)
print("DFS solution is ", searchingUsingDFS)
print("UCS solution is ", searchingUsingUCS, "\twith cost=", pathCost)
print("ASTAR solution is ", searchingUsingASTAR, "\twith cost=", pathCostWithHeuristic)
print("Greedy solution is ", searchingUsingGreedy, "\twith cost=", heuristicCost)
