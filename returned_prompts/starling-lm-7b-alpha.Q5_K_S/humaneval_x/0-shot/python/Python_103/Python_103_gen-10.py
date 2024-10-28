
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    if n > m:
        return -1
    avg = (n + m) / 2
    bin_avg = bin(avg)[2:]
    return "0b" + bin_avg

# Test cases
print(rounded_avg(1, 5))  # "0b11"
print(rounded_avg(7, 5))  # -1
print(rounded_avg(10, 20))  # "0b1111"
print(rounded_avg(20, 33))  # "0b11010"

# More test cases
print(rounded_avg(0, 1))  # "0b1"
print(rounded_avg(1, 1))  # "0b1"
print(rounded_avg(2, 2))  # "0b1"
print(rounded_avg(3, 3))  # "0b1"
print(rounded_avg(3, 4))  # "0b10"
print(rounded_avg(4, 4))  # "0b10"
print(rounded_avg(4, 5))  # "0b10"
print(rounded_avg(5, 5))  # "0b1"
print(rounded_avg(5, 6))  # "0b10"
print(rounded_avg(6, 6))  # "0