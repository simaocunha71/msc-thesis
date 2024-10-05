    result = []
    current_level = n
    while current_level > 0:
        result.append(current_level)
        if current_level % 2 == 0:
            current_level += 2
        else:
            current_level += 1
    return result[::-1]  # Reverse the list to match the required order

