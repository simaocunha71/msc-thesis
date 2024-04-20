"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""
def is_num_decagonal(n):
    return n in (int(factorial(10)/factorial(9)))

if __name__ == "__main__":
    # Example:
    print("is_num_decagonal(3) = ", is_num_decagonal(3))
