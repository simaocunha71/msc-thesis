def median_trapezium(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if len(sides) % 2 == 0:
        return (sides[len(sides) // 2 - 1] + sides[len(sides) // 2]) / 2
    else:
        return sides[len(sides) // 2]  # median is the middle value when the number of sides is odd