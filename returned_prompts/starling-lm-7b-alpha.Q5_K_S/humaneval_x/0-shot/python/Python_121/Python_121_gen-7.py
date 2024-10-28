
def solution(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum

# Test cases:
print(solution([5, 8, 7, 1]))  # Expected: 12
print(solution([3, 3, 3, 3, 3]))  # Expected: 9
print(solution([30, 13, 24, 321]))  # Expected: 0



# Other Solution
def solution(lst):
    return sum(lst[i] for i,x in enumerate(lst) if i%2==0 and x%2!=0)


# Test cases:
print(solution([5, 8, 7, 1]))  # Expected: 12
print(solution([3, 3, 3, 3, 3]))  # Expected: 9
print(solution([30, 13, 24, 321]))  # Expected: 0


# Other Solution
def solution(lst):
    return sum(lst[i] for i,x in enumerate(lst) if i%2==0 and x%2!=0)


# Test cases:
print(solution([5, 8, 7, 1]))  # Expected: 12
print(solution([3, 3, 3, 3, 3]))  # Expected: 9
print(solution([30, 13, 24, 321]))  # Expected: 0

# Other Solution
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0)

# Test cases:
print(solution([5, 8, 7, 1]))  # Expected: 12
print(solution([3, 3, 3, 3, 3]))  # Expected: 