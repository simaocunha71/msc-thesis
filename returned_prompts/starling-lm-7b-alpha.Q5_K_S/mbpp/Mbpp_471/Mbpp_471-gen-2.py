"""
def find_remainder(arr, n):
    def product(i, j):
        if i == j: return arr[i]
        else: return (product(i + 1, j) % n) * (arr[i] % n) % n
    return product(0, len(arr) - 1) % n
"""

def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product % n) * (num % n) % n
    return product % n

print(find_remainder([100, 10, 5, 25, 35, 14], 11))

# Output: 9


# Explanation
# In this program, we need to find the product of the array multiplication modulo n.

# Here, n is the number of modulo.
# So, we need to multiply all the elements of the array with the modulo n.

# To multiply all the elements of the array with the modulo n, we need to find the product of all the elements of the array.

# Here, product is the variable to store the product of the array. We initialize it with 1.

# Then, we use a for loop to iterate through each element of the array. In each iteration, we multiply the product with the current element of the array and modulo n.

# Finally, we return the product modulo n.

# Time Complexity: O(n)
# Space Complexity: O(1)
# The time complexity of the program is O(n) as we are using a for loop to iterate through each element of the array.

# The space complexity of the program is O(1) as we are not using any extra space that depends on the input size.

# In this program, we are finding the product of the array multiplication modulo n.

# The time complexity of the program is O(n) as we are using a for loop to iterate through each element of the array.

# The space complexity of the program is O(1) as we are not using any extra space that depends on the input size.

# The