
def pathCost(path):                 # for UCS
    totalCost = 0
    for (node, cost) in path:
        totalCost += cost
    return totalCost


def heuristicCost(path):            # for Greedy
    lastNode = path[-1][0]
    h_Cost = H_Table[lastNode]
    return h_Cost, lastNode


def pathCostWithHeuristic(path):    # for AStar
    lastNode = path[-1][0]
    h_Cost = H_Table[lastNode]
    f_Cost = pathCost(path) + h_Cost
    return f_Cost, lastNode


H_Table = {     # for AStar & Greedy
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}
