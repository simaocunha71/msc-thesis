def difference(n):
    # Calculate the sum of cubes of the first n natural numbers
    sum_cubes = sum([i**3 for i in range(1, n+1)])
    # Calculate the sum of the first n natural numbers
    sum_natural_numbers = sum([i for i in range(1, n+1)])
    # Calculate the difference between the two sums
    result = sum_cubes - sum_natural_numbers
    return result