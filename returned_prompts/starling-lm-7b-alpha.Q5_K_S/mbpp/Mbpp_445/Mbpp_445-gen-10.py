def index_multiplication(tup1, tup2):
    if len(tup1) != len(tup2):
        return None
    else:
        result = []
        for i in range(len(tup1)):
            result.append((tup1[i] * tup2[i]))
        return tuple(result)


# Driver code
print(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))))


"""

"""

# Time complexity : O(n), where n = length(tup1)
# Space complexity : O(n)


"""
This problem can be solved by iterating through each tuple and multiplying the elements at the same index. The result is stored in a new tuple. If the lengths of the two tuples are different, the function returns None. Otherwise, it returns the resulting tuple.

In the given code, the function index_multiplication takes two tuples, tup1 and tup2, as parameters. It first checks if the lengths of the tuples are equal. If they are not, it returns None. Otherwise, it initializes an empty list, result, to store the multiplied elements.

Then, it iterates through the range of the length of tup1 using a for loop. For each index i, it multiplies the elements at index i of tup1 and tup2 and appends the result to the result list. Finally, it converts the result list to a tuple and returns it.

In the driver code, the function is called with two tuples as arguments. The result is printed using the print function.

The time complexity of this solution is O(n), where n is the length of tup1. This is because the function iterates through each element of tup1. The space complexity is also O(n), as the result list can grow up to the size of tup1.

"""

# Python3 program to find if a number is prime or not

# Function to check if a number is prime or not
def isPrime(n):
    # Corner cases
    if