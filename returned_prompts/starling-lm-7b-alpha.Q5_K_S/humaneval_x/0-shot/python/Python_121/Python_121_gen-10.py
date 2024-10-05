
def solution(lst):
    even_position_odd_sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            even_position_odd_sum += lst[i]
    return even_position_odd_sum

# Alternative solution using list comprehension
def solution(lst):
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])

# Alternative solution using filter() function
def solution(lst):
    return sum(filter(lambda x: x % 2 != 0 and (x / 2) % 2 == 0, lst))

# Alternative solution using generator expression
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0)

# Testing the function
print(solution([5, 8, 7, 1]))  # Returns: 12
print(solution([3, 3, 3, 3, 3]))  # Returns: 9
print(solution([30, 13, 24, 321]))  # Returns: 0

# Testing the alternative functions
print(solution([5, 8, 7, 1]))  # Returns: 12
print(solution([3, 3, 3, 3, 3]))  # Returns: 9
print(solution([30, 13, 24, 321]))  # Returns: 0
print(solution([30, 13, 24, 321]))  # Returns: 0

# Testing the function with an empty list
print(solution([]))  # Returns: 0

# Testing the function with a list of all even numbers
print(solution([2, 4, 6, 8]))  # Returns: 0

# Testing the function with a list of all odd numbers
print(solution([1,