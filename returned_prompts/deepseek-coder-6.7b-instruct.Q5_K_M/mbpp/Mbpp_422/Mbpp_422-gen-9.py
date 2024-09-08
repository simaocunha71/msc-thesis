def find_Average_Of_Cube(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    average = sum_of_cubes/n
    return average

print(find_Average_Of_Cube(2))

# Output: 4.5

"""
Explanation:
The sum of cubes of first 2 natural numbers is 1^3 + 2^3 = 1 + 8 = 9
The average of cubes of first 2 natural numbers is 9/2 = 4.5
"""





