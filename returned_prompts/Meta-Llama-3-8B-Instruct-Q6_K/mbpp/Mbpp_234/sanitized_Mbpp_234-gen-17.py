def volume_cube(side_length):
    try:
        side_length = float(side_length)
        return side_length ** 3
    except ValueError:
        return "Error: Input must be a number"