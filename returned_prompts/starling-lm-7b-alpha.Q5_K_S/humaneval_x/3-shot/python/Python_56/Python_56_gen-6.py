    left = 0
    right = 0

    for char in brackets:
        if char == "<":
            left += 1
        elif char == ">":
            right += 1
        else:
            raise ValueError("Invalid bracket")

    return left == right


