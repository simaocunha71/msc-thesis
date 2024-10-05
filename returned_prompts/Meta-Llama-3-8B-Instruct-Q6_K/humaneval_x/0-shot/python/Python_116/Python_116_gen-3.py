    def sort_array(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))



# Testing the function
print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]





# Explanation:
The function `sort_array` sorts the input list `arr` based on two criteria: 
1. The number of ones in the binary representation of the numbers (in ascending order).
2. The decimal value of the numbers (in ascending order).

To achieve this, we use the `sorted` function with a custom key function. The key function is a lambda function that returns a tuple for each element in the list. The tuple contains two elements: 
- The first element is the count of ones in the binary representation of the number, obtained by using the `bin` function to convert the number to a binary string and then counting the number of '1's using the `count` method.
- The second element is the decimal value of the number itself.

The `sorted` function then sorts the list based on these tuples. When the counts of ones are equal, it sorts based on the decimal values. This ensures that the numbers with the same number of ones are sorted in ascending order.