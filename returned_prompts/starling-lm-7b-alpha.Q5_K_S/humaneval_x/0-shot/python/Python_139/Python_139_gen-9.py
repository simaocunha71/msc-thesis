
def special_factorial(n):
    if n <= 0:
        return 0
    else:
        return 1 if n == 1 else n * special_factorial(n-1)

# Test cases
print(special_factorial(4))  # 288
print(special_factorial(3))  # 6
print(special_factorial(2))  # 2
print(special_factorial(1))  # 1
print(special_factorial(0))  # 0


def special_factorial_test():
    assert special_factorial(4) == 288
    assert special_factorial(3) == 6
    assert special_factorial(2) == 2
    assert special_factorial(1) == 1
    assert special_factorial(0) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    special_factorial_test()


