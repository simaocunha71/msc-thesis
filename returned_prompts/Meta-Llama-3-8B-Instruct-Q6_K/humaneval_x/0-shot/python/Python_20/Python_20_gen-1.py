    # Find the closest pair of numbers in the list
    # Use the math library to calculate the absolute difference between each pair of numbers
    # Sort the list of numbers and the list of differences
    # Then return the pair of numbers with the smallest difference
    import math

    # Calculate the differences between each pair of numbers
    differences = [(numbers[i], numbers[i+1], abs(numbers[i]-numbers[i+1])) for i in range(len(numbers)-1)]

    # Sort the list of differences
    differences.sort(key=lambda x: x[2])

    # Return the pair of numbers with the smallest difference
    return (differences[0][0], differences[0][1]) if differences[0][0] != differences[0][1] else (differences[0][0], differences[0][0])
    # If the pair of numbers is the same, return the pair twice

    # You can also use the min function with a key function
    # return min((numbers[i], numbers[i+1]) for i in range(len(numbers)-1), key=lambda x: abs(x[0]-x[1]))

    # You can also use the sorted function with a key function
    # return tuple(sorted([numbers[i] for i in range(len(numbers)-1)], key=lambda x: [i for i in range(len(numbers)-1) if abs(x-numbers[i]) == min([abs(x-numbers[i]) for i in range(len(numbers)-1)])][0]))

    # You can also use the bisect module
    # import bisect
    # numbers.sort()
    # idx = bisect.bisect_left(numbers, numbers[0] + (numbers[1] - numbers[0]) / 2)
    # if idx == len(numbers):
    #     return (numbers[-1], numbers[0])
    # elif idx == 0:
    #     return (numbers[0], numbers[1])
    # else:
    #     return (numbers[idx-1], numbers[idx]) if abs(numbers[idx]-numbers[idx-1]) < abs(numbers[idx+1]-numbers[idx]) else (numbers[idx], numbers[idx+1])

    # You can also use the numpy library
    # import numpy as np
    # numbers = np.array(numbers)
    # return tuple(numbers[np.argsort(np.abs(numbers[None]-numbers[:, None])).flatten()[:2]])

    # You can also use the