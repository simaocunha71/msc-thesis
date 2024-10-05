
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)

# Test cases
print(solution([5, 8, 7, 1]))  # 12
print(solution([3, 3, 3, 3, 3]))  # 9
print(solution([30, 13, 24, 321]))  # 0
print(solution([10, 20, 30, 40, 50, 60]))  # 10
print(solution([11, 21, 31, 41, 51, 61]))  # 11
<jupyter_output>
12
9
0
10
11
<jupyter_text>
