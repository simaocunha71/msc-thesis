    if not all(isinstance(i, int) for i in [x, y, z]):
        return False

    return (x + y == z) or (x + z == y) or (y + z == x)  # Check for all possible combinations


