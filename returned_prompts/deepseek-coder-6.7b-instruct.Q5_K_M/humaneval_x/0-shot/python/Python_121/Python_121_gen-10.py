
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 1:
            sum += lst[i]
    return sum


# Test cases
print(solution([5, 8, 7, 1]))  # 12
print(solution([3, 3, 3, 3, 3]))  # 9
print(solution([30, 13, 24, 321]))  # 0
print(solution([10, 20, 30, 40, 50]))  # 30
print(solution([2, 3, 4, 5, 6, 7]))  # 14
print(solution([12, 24, 36, 48, 60, 72, 84]))  # 144
print(solution([5, 10, 15, 20, 25, 30]))  # 40
print(solution([1, 2, 1, 2, 1, 2, 1, 2]))  # 4
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 25
print(solution([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 0
<jupyter_output>
12
9
0
30
14
144
40
4
25
0
<jupyter_text>
Problem 4
<jupyter_code>
