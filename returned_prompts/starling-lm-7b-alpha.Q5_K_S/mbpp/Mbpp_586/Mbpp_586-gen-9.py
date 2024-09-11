def split_Arr(arr,n):
    return arr[n:]+arr[:n]

# Testing the function
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
print("Test Passed!")







"""
The split_Arr function takes in two parameters, an array and a number.

In the function, we use array slicing to split the array at the nth index, and append the first part to the end of the array.

To test the function, we use the assert statement to check if the output of the function is equal to the expected result.

If the assertion is true, we print "Test Passed!" to the console.
"""

"""
The function split_Arr() takes in two parameters: an array and a number. It uses array slicing to split the array at the nth index and then appends the first part of the array to the end. The function returns the modified array.

In the provided example, the function split_Arr([12,10,5,6,52,36],2) is called, passing the array [12,10,5,6,52,36] and the number 2 as arguments. The function will split the array at the 2nd index (the index of 5) and append the first part of the array to the end.

The expected result of this function call is [5,6,52,36,12,10]. The assert statement checks if the actual result of the function call is equal to the expected result. If the assertion is true, the message "Test Passed!" is printed to the console.
"""

"""
To test the function, we use the assert statement to compare the actual result of the function with the expected result. If the assertion is true, it means that the function is working correctly, and we print "Test Passed!" to the console.

In this case, the actual result of the function call split_Arr([12,10,5,6,52,36],2) is [5,6,52,36,12,10], which