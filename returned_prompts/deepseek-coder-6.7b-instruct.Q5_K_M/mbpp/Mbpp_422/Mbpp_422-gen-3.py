def find_Average_Of_Cube(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    avg_of_cubes = sum_of_cubes / n
    return avg_of_cubes

print(find_Average_Of_Cube(2))

"""
Output:
4.5
"""

"""
Explanation:
Here we are finding the sum of cubes of first n natural numbers, then dividing it by n to get the average. The sum of cubes of first n natural numbers is given by (n*(n+1)/2)^2.
"""

