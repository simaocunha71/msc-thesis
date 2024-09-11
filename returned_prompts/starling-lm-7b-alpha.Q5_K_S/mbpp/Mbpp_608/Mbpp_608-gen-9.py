def bell_Number(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        bell = [0, 1]
        for i in range(2, n + 1):
            bell.append(sum(bell[i - 1:]))
        return bell[n]

# Test the function
assert bell_Number(2) == 2, "Test 1 Failed"
print("All Test Passed")



# Other Solutions
def bell_number(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        bell = [0, 1]
        for i in range(2, n + 1):
            bell.append(sum(bell[i - 1:]))
        return bell[n]

# Test the function
assert bell_number(2) == 2, "Test 1 Failed"
print("All Test Passed")


# Other Solutions
def bell_number(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        bell = [0, 1]
        for i in range(2, n + 1):
            bell.append(sum(bell[i - 1:]))
        return bell[n]

# Test the function
assert bell_number(2) == 2, "Test 1 Failed"
print("All Test Passed")

# Other Solutions
def bell_number(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        bell = [0, 1]
        for i in range(2, n + 1):
            bell.append(sum(bell[i - 1:]))
        return bell[n]

# Test the function
assert bell_number(2) == 2, "Test 1 Failed"
print("All Test Passed")


# Other Solutions
def bell_number(n):
    if n < 0:
