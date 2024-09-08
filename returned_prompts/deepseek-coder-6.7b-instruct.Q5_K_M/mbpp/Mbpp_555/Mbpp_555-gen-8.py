def difference(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    sum_of_numbers = sum([i for i in range(1, n+1)])
    return sum_of_cubes - sum_of_numbers

# Test
print(difference(3))  # 30

# Alternative Solution
def difference(n):
    return sum([i**3 for i in range(1, n+1)]) - sum([i for i in range(1, n+1)])

# Test
print(difference(3))  # 30

