def find_sum(l):
    # Create a set from the given list
    s = set(l)
    # Initialize sum to 0
    sum = 0
    # Iterate over the set and add each element to the sum
    for i in s:
        sum += i
    # Return the sum
    return sum

# Test Case
print(find_sum([1,2,3,1,1,4,5,6]))



# Correct Solution:
def find_sum(l):
    # Create a set from the given list to remove all duplicates
    s = set(l)
    # Initialize sum to 0
    sum = 0
    # Iterate over the set and add each element to the sum
    for i in s:
        sum += i
    # Return the sum
    return sum

# Test Case
print(find_sum([1,2,3,1,1,4,5,6]))  # Expected Output: 21



# Explanation: 
# To find the sum of non-repeated elements in a given list, we can follow these steps:
# 1. Create a set from the given list to remove all duplicates. This is because the sum function will only count the first occurrence of each element.
# 2. Initialize a variable sum to 0.
# 3. Iterate over the set and add each element to the sum.
# 4. Return the sum.
# In the provided solution, we have implemented these steps in the find_sum function. The function takes a list as input and returns the sum of its non-repeated elements.


"""
Here's an example test case to verify the correctness of the find_sum function:

print(find_sum([1,2,3,1,1,4,5,6]))  # Expected Output: 21

In this test case, the find_sum function is called with the list [1,2,3,1,1,4,5,6]. The function correctly removes the duplicate elements (1 and 2) and calculates the sum of the remaining non-repeated elements (3, 4, 5, and 6). The