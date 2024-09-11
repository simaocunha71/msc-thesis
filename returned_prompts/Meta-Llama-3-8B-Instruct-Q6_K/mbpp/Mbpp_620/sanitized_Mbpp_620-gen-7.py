def largest_subset(nums):
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                graph[i].append(j)
                graph[j].append(i)
    visited = set()
    max_size = 0
    for node in graph:
        if node not in visited:
            size = 0
            stack = [node]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    size += 1
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            max_size = max(max_size, size)
    return max_size