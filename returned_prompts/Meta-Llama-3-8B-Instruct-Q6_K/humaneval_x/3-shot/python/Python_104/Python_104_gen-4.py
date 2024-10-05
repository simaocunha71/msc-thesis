    return sorted([i for i in x if all(int(digit) % 2 != 0 for digit in str(i))])  # using list comprehension and generator expression
    # or
    return sorted([i for i in x if not any(int(digit) % 2 == 0 for digit in str(i))])  # using list comprehension and generator expression
    # or
    result = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)  # using for loop and append to list
    # or
    result = []
    for num in x:
        if not any(int(digit) % 2 == 0 for digit in str(num)):
            result.append(num)
    return sorted(result)  # using for loop and append to list
    # or
    return sorted([i for i in x if all(int(digit) % 2 != 0 for digit in str(i))])  # using list comprehension
    # or
    return sorted([i for i in x if not any(int(digit) % 2 == 0 for digit in str(i))])  # using list comprehension
    # or
    result = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)  # using for loop
    # or
    result = []
    for num in x:
        if not any(int(digit) % 2 == 0 for digit in str(num)):
            result.append(num)
    return sorted(result)  # using for loop
    # or
    return sorted([i for i in x if all(int(digit) % 2 != 0 for digit in str(i))])  # using list comprehension
    # or
    return sorted([i for i in x if not any(int(digit) % 2 == 0 for digit in str(i))])  # using list comprehension
    # or
    result = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)  # using for loop
    # or
    result = []
    for num in x:
        if not any(int(digit) % 