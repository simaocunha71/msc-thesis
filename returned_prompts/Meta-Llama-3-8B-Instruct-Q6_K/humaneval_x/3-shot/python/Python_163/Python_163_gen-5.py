    return [i for i in range(min(a, b), max(a, b)+1) if i % 2 == 0] if a <= b else [i for i in range(max(a, b), min(a, b)-1, -1) if i % 2 == 0]  # check the condition a <= b and generate the list accordingly


