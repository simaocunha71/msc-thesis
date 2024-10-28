    result = [max(numbers[:i+1]) for i in range(len(numbers))]
    return result
    # Alternatively, you can use deque from collections module for efficient implementation
    # from collections import deque
    # d = deque()
    # result = [max(d) for _ in numbers]
    # for num in numbers:
    #     d.append(num)
    #     d.popleft()
    # return result
    # Or using numpy
    # import numpy as np
    # return np.maximum.accumulate(numbers)

# Testing the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]




