    # 0 for not visited, 1 for visited
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = [[[0, 0, 1]]]
    result = []
    while queue:
        point = queue.pop(0)
        visited[point[0][0]][point[0][1]] = 1
        result.append(grid[point[0][0]][point[0][1]])
        if len(result) == k:
            break
        for i in range(len(point)):
            new_point = point[i][:]
            if new_point[0] + 1 < len(grid) and visited[new_point[0] + 1][new_point[1]] == 0:
                new_point[0] += 1
                queue.append(new_point)
            if new_point[0] - 1 >= 0 and visited[new_point[0] - 1][new_point[1]] == 0:
                new_point[0] -= 1
                queue.append(new_point)
            if new_point[1] + 1 < len(grid[0]) and visited[new_point[0]][new_point[1] + 1] == 0:
                new_point[1] += 1
                queue.append(new_point)
            if new_point[1] - 1 >= 0 and visited[new_point[0]][new_point[1] - 1] == 0:
                new_point[1] -= 1
                queue.append(new_point)
    return result


