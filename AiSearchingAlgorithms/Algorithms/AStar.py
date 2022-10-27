from Calc.calcCosts import pathCostWithHeuristic


def aStar(graph, startNode, goalNode):
    visitedNodes = []
    priorityQueue = [[(startNode, 0)]]  # [0] list of lists(paths)
    while priorityQueue:
        priorityQueue.sort(key=pathCostWithHeuristic)
        path = priorityQueue.pop(0)  # [1] pop FirstInputPath to check it
        currentNode = path[-1][0]  # [2] return lastNode
        if currentNode in visitedNodes:  # [2.1] if it was previously visited pop another path
            continue
        visitedNodes.append(currentNode)
        if currentNode == goalNode:  # [2.2] if it was the goalNode stop looping & return the path(answer)
            return path
        else:
            adjacentNodes = graph.get(currentNode, [])  # [3] return currentNode's adjacentNodes if exist else return []
            for (node, cost) in adjacentNodes:
                newPath = path.copy()  # take a copy from currentPath
                newPath.append((node, cost))  # append to it one adjacentNode
                priorityQueue.append(newPath)  # append this newPath to queue
