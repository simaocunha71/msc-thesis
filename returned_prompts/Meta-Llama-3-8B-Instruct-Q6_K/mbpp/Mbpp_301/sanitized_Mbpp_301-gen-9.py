def dict_depth(d):
    depth = 1
    max_depth = 1
    stack = [(d, 1)]
    while stack:
        node, curr_depth = stack.pop(0)
        if isinstance(node, dict):
            for key, value in node.items():
                stack.append((value, curr_depth + 1))
            max_depth = max(max_depth, curr_depth + 1)
        else:
            depth = curr_depth
    return max_depth