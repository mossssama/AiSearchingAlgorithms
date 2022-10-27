def dfs(graph, startNode, goalNode):
    visitedNodes = []
    stack = [[startNode]]           # [0] list of lists(paths)
    while stack:
        path = stack.pop()         # [1] pop LastInputPath to check it
        currentNode = path[-1]      # [2] return lastNode
        if currentNode in visitedNodes:  # [2.1] if it was previously visited pop another path
            continue
        visitedNodes.append(currentNode)
        if currentNode == goalNode:      # [2.2] if it was the goalNode stop looping & return the path(answer)
            return path
        else:
            adjacentNodes = graph.get(currentNode, [])  # [3] return currentNode's adjacentNodes if exist else return []
            for node in adjacentNodes:
                newPath = path.copy()       # take a copy from currentPath
                newPath.append(node)        # append to it one adjacentNode
                stack.append(newPath)       # append this newPath to stack
