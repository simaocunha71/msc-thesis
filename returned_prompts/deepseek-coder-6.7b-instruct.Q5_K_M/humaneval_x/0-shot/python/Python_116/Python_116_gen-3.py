
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

print(sort_array([1, 5, 2, 3, 4]))
print(sort_array([-2, -3, -4, -5, -6]))
print(sort_array([1, 0, 2, 3, 4]))

# the lambda function in the key parameter is a function that returns a tuple.
# The first element of the tuple is the count of '1' in the binary representation of the number.
# The second element of the tuple is the number itself, which is used as a tie breaker when the counts are equal.
# The sorted function is called with the key parameter set to the lambda function. This means that the sorted function will sort the elements of the array based on the tuple returned by the lambda function.
# The sorted function returns a new list that contains the sorted elements of the array.
# The original array is not modified.
# The sorted function sorts the elements of the array in ascending order by default.
# The sorted function uses the less than operator to compare the elements of the array.
# The sorted function is stable, which means that it preserves the relative order of the elements that compare equal.
# The sorted function returns a new list that contains the sorted elements of the array.
# The original array is not modified.

# the bin function returns the binary representation of the number as a string.
# The count method of a string returns the number of occurrences of a substring in the string.
# In this case, it returns the number of '1's in the binary representation of the number.
# The lambda function returns a tuple that is used to sort the elements of the array.
# The first element of the tuple is the count of '1's in the binary representation of the number.
# The second element of the tuple is the number itself.
# The sorted function sorts the elements of the array based on the tuple returned by the lambda function.
# The sorted function returns a new list that contains the sorted elements of the array.
# The original array is not modified.
# The sorted function uses the less than operator to compare the elements of the array.
# The sorted