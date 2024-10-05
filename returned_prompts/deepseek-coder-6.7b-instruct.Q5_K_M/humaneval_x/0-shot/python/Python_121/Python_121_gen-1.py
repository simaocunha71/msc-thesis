
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)


# Tests:
print(solution([5, 8, 7, 1]))  # 12
print(solution([3, 3, 3, 3, 3]))  # 9
print(solution([30, 13, 24, 321]))  # 0
print(solution([1, 1, 1, 1, 1, 1]))  # 1
print(solution([2, 2, 2, 2, 2, 2]))  # 0
print(solution([1, 2, 3, 4, 5, 6]))  # 4
print(solution([10, 20, 30, 40, 50, 60]))  # 0
print(solution([20, 20, 10, 10, 10, 10]))  # 10
print(solution([10, 20, 30, 40, 50, 60]))  # 0
print(solution([2, 2, 2, 2, 2, 2]))  # 0
print(solution([1, 2, 3, 4, 5, 6]))  # 4
print(solution([10, 20, 30, 40, 50, 60]))  # 0
print(solution([20, 20, 10, 10, 10, 10]))  # 10
print(solution([10, 20, 30, 40, 50, 60]))  # 0
print(solution([2, 2, 2, 2, 2, 2]))  # 0
print(solution([1, 2, 3, 4, 5, 6]))  # 4
print(solution([