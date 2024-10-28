def rectangle_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        return "Error: Both length and width must be numbers."
    if length <= 0 or width <= 0:
        return "Error: Both length and width must be positive numbers."
    if length > 1000 or width > 1000:
        return