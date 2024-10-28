    def solution(lst):
        sum_odd_elements = 0
        for i in range(len(lst)):
            if i % 2 == 0 and lst[i] % 2 != 0:
                sum_odd_elements += lst[i]
        return sum_odd_elements
    print(solution([5, 8, 7, 1]))  # Output: 12
    print(solution([3, 3, 3, 3, 3]))  # Output: 9
    print(solution([30, 13, 24, 321]))  # Output: 0
    print(solution([1, 3, 5, 7]))  # Output: 12
    print(solution([2, 4, 6, 8]))  # Output: 0
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 18
    print(solution([11, 12, 13, 14, 15]))  # Output: 24
    print(solution([1, 3, 5, 7, 9, 11, 13, 15]))  # Output: 39
    print(solution([2, 4, 6, 8, 10, 12, 14, 16, 18]))  # Output: 0
    print(solution([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))  # Output: 90
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))  # Output: 95
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))  # Output: 102
    print(solution([1, 2, 3, 4, 5, 6, 7, 