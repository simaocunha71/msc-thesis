def square_perimeter(side_length):
    if not isinstance(side_length, int):
        return "Error: side length must be an integer"
    if side_length <= 0:
        return "Error: side length must be a positive integer"
    return 4 * side_length