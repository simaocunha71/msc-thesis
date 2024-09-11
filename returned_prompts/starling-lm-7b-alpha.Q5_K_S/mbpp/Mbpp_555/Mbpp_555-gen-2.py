def difference(n):
    sum_cube = 0
    sum_natural = 0
    for i in range(1, n + 1):
        sum_cube += i ** 3
        sum_natural += i
    return sum_cube - sum_natural


def test_difference():
    assert difference(3) == 30
    print("All tests passed")


test_difference()


# Explanation:
# The function takes an input parameter n, which represents the number of natural numbers to consider. It initializes two variables, sum_cube and sum_natural, to store the sum of cubes and the sum of natural numbers, respectively. 
# The function uses a for loop to iterate through each number from 1 to n (inclusive). For each iteration, it adds the cube of the current number to sum_cube and adds the current number itself to sum_natural. 
# After the loop is complete, the function returns the difference between sum_cube and sum_natural, which represents the desired result. 
# The test_difference function is used to verify the correctness of the implementation by comparing the result of the function with the expected value of 30 for the input of 3. 
# If all tests pass, the message "All tests passed" is printed, indicating that the function is working as expected. 
# This approach allows for easy addition of more test cases to ensure the function's correctness for different inputs. 
"""

"""


def difference(n):
    sum_cube = 0
    sum_natural = 0
    for i in range(1, n + 1):
        sum_cube += i ** 3
        sum_natural += i
    return sum_cube - sum_natural

def test_difference():
    assert difference(3) == 30
    print("All tests passed")

test_difference()

"""


# Explanation:
# The function takes an input parameter n, which represents the number of natural numbers to consider. It initializes two variables, sum_cube and sum_natural, to store the sum of cubes and the sum of natural numbers, respectively. 
# The function uses