    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


# Run tests
print(below_zero([1, 2, 3]))  # Expected False
print(below_zero([1, 2, -4, 5]))  # Expected True


# More tests
print(below_zero([10, 20, -30, 40]))  # Expected True
print(below_zero([100, 200, -300, 400]))  # Expected False
print(below_zero([]))  # Expected False


# Extra credit
print(below_zero([-10, -10]))  # Expected True
print(below_zero([-100, -100, -100]))  # Expected False


# Extra extra credit
print(below_zero([100, 200, 300, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000