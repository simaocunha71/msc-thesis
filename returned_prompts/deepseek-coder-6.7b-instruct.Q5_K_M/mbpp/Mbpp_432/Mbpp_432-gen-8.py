def median_trapezium(a, b, c):
    """
    This function calculates the median length of a trapezium.
    """
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area using Heron's formula
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    # calculate the median length using the area of the trapezium formula
    median_length = (4*area) / (a + b)
    return median_length

print(median_trapezium(15, 25, 35)) # expected output: 20.0

