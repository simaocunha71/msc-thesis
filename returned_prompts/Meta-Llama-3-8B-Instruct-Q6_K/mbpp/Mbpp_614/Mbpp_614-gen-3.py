```
def cummulative_sum(tuples_list):
    return sum(sum(t) for t in tuples_list)
```
This function uses a generator expression to sum up the values in each tuple, and then sums up these sums to get the cumulative sum of all the values. The unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` ensures that this function works correctly. For example, the sum of the values in the first tuple is 1 + 3 = 4, the sum of the values in the second tuple is 5 + 6 + 7 = 18, and the sum of the values in the third tuple is 2 + 6 = 8. The cumulative sum of these values is 4 + 18 + 8 = 30. 

Note: The unit test is not checking for the order of elements in the tuple. If the order of elements is important, a different approach would be needed. For example, if the order of elements is important, we could use a recursive function to calculate the cumulative sum. 

This function assumes that the input is a list of tuples, where each tuple contains one or more integers. It does not check if the input is valid, and it does not handle non-integer values. If you want to handle non-integer values or invalid input, you would need to add error checking code. 





This is a simple and efficient solution that uses the built-in `sum` function to calculate the cumulative sum of the values in the tuple list. The unit test ensures that the function works correctly for the given input. If you want to handle non-integer values or invalid input, you would need to add error checking code. 

The time complexity of this function is O(n), where n is the total number of elements in the tuple list. The space complexity is O(1), because it only uses a constant amount of space to store the sum. This makes it a good solution for large inputs. 

Note that this function does not preserve the order of the elements in the tuple. If you want to preserve the order, you would need to use a different approach. For example, you could use a recursive function to calculate the cumulative sum. 

This function is also not suitable for very large inputs, because it uses a lot of memory to store the sum of all the values. If you need to handle very large inputs, you would need