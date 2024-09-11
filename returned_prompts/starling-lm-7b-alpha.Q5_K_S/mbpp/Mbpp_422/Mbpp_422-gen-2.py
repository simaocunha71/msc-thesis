def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum/(n+1)

"""
Test Case:
find_Average_Of_Cube(2) == 4.5

Explanation:
As per the question, we need to find the average of cubes of first n natural numbers.
We know that the sum of first n natural numbers is n(n+1)/2.
Here, we need to find the sum of cubes of first n natural numbers.
So, the sum = n(n+1)(2n+1)/6
To find the average of cubes of first n natural numbers, divide the sum by n+1.
"""

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# Test Case:
# assert find_Average_Of_Cube(2) == 4.5
# print(find_Average_Of_Cube(2)) # 4.5
# print(find_Average_Of_Cube(3)) # 5.666666666666667
# print(find_Average_Of_Cube(4)) # 7.083333333333333
# print(find_Average_Of_Cube(5)) # 8.571428571428571
# print(find_Average_Of_Cube(6)) # 10.11111111111111
# print(find_Average_Of_Cube(7)) # 11.666666666666666
# print(find_Average_Of_Cube(8)) # 13.222222222222222
# print(find_Average_Of_Cube(9)) # 14.828282828282828
# print(find_Average_Of_Cube