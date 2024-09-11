def unique_product(lst):
    """
    Function to calculate the product of the unique numbers in a given list
    """
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product

def test_unique_product():
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000

test_unique_product()

# Here's one way to solve the problem:
# - First, create a set from the given list to remove any duplicates
# - Then, initialize a product variable with a value of 1
# - Iterate over the unique_nums set and multiply the product by each number
# - Finally, return the product

# Note: The set() function in Python automatically removes duplicates from a list
# This means that if a number appears multiple times in the original list, it will only appear once in the set

# The test_unique_product() function is used to verify that the unique_product() function is working correctly
# It asserts that the function correctly calculates the product of the unique numbers in the given list

# Running the test_unique_product() function will check if the assertion is true and print "OK" if it is
# Otherwise, it will print an error message indicating the expected and actual results

# This solution has a time complexity of O(n), where n is the length of the input list
# The set() function has a time complexity of O(n) and the for loop also has a time complexity of O(n)
# The multiplication operation in the loop has a time complexity of O(1)
# Therefore, the overall time complexity of the unique_product() function is O(n)

# The space complexity of the unique_product() function is O(n)
# The set() function requires additional memory to store the unique numbers, and the product variable also requires memory
# Since the length of the input list is n, the space complexity is O(n)

# Here's a step-by-step breakdown of the code:

# Step 1: