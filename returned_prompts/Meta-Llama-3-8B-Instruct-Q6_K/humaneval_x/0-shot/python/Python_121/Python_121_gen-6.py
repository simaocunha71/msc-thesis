def solution(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum
# test the function
print(solution([5, 8, 7, 1]))  # 12
print(solution([3, 3, 3, 3, 3]))  # 9
print(solution([30, 13, 24, 321]))  # 0
print(solution([1, 3, 5, 7, 9]))  # 25
print(solution([2, 4, 6, 8]))  # 0
print(solution([1]))  # 1
print(solution([2, 3, 4, 5, 6, 7, 8, 9]))  # 9
print(solution([10, 12, 14, 16]))  # 0
print(solution([1, 1, 1, 1]))  # 2
print(solution([2, 2, 2, 2]))  # 0
print(solution([1, 1, 1, 1, 1]))  # 2
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 9
print(solution([2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 0
print(solution([1, 2, 3, 4, 5]))  # 9
print(solution([1, 2, 3, 4, 5, 6, 7]))  # 9
print(solution([2, 3, 4, 5, 6]))  # 0
print(solution([1, 2]))  # 1
print(solution([1, 2, 3]))  # 2
print(solution([1, 2, 3, 4]))  # 0
print(solution([1, 2, 3, 4, 5, 6]))  # 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8