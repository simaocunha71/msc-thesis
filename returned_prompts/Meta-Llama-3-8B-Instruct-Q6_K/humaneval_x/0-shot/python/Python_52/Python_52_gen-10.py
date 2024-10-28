def below_threshold(l, t):
    return all(x < t for x in l)
    
    # test the function
    print(below_threshold([1, 2, 4, 10], 100))  # True
    print(below_threshold([1, 20, 4, 10], 5))  # False
    print(below_threshold([1, 2, 3, 4], 5))  # True
    print(below_threshold([100, 100, 100, 100], 100))  # True
    print(below_threshold([101, 101, 101, 101], 100))  # False

    # Use the function with a list comprehension
    numbers = [1, 2, 3, 4, 5]
    result = all(x < 5 for x in numbers)
    print(result)  # True

    # Use the function with a generator expression
    result = all(x < 5 for x in (1, 2, 3, 4, 5))
    print(result)  # True

    # Use the function with a list comprehension and a condition
    numbers = [1, 2, 3, 4, 5]
    result = all(x < 5 for x in numbers if x % 2 == 0)
    print(result)  # True

    # Use the function with a generator expression and a condition
    result = all(x < 5 for x in (1, 2, 3, 4, 5) if x % 2 == 0)
    print(result)  # True

    # Use the function with a list comprehension and multiple conditions
    numbers = [1, 2, 3, 4, 5]
    result = all(x < 5 and x % 2 == 0 for x in numbers)
    print(result)  # True

    # Use the function with a generator expression and multiple conditions
    result = all(x < 5 and x % 2 == 0 for x in (1, 2, 3, 4, 5))
    print(result)  # True
    # test the function with a empty list
    print(below_threshold([], 100))  # True
    # test the function with a list of single element
    print(below_threshold([100],