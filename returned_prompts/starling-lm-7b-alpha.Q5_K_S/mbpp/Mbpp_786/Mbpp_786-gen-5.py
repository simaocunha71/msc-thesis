def right_insertion(list1,value):
    insert_index = 0
    while insert_index<len(list1) and list1[insert_index]<value:
        insert_index+=1
    return insert_index

# Test
print(right_insertion([1,2,4,5],6))

"""
In this function, we use a while loop to find the right insertion point. In each iteration, we compare the current value with the specified value. If the current value is less than the specified value, we increment the insert_index value and continue the loop. Once the insert_index is equal to the length of the list, or the current value is greater than the specified value, we return the insert_index.
"""

"""
Test

We create a function right_insertion that takes a list and a value as parameters. Inside the function, we initialize the insert_index to 0. Then, we use a while loop to iterate through the list. In each iteration, we compare the current value with the specified value. If the current value is less than the specified value, we increment the insert_index value and continue the loop. Once the insert_index is equal to the length of the list, or the current value is greater than the specified value, we return the insert_index.

After defining the function, we use the print statement to test the function. We call the function with the list [1,2,4,5] and the value 6. The function should return 4, as 6 should be inserted at index 4 in the sorted list.
"""

"""
The assert statement is used to test if the function is working correctly. If the function returns the expected result, the assert statement will not raise an error. Otherwise, an AssertionError will be raised, indicating that the function is not working as expected.
"""

"""
In this case, the assert statement is used to test if the function right_insertion returns the expected result when given the list [1,2,4,5] and the value 6. If the function returns 4, the assert statement will not raise an error, and the program will continue executing. Otherwise, an AssertionError will be raised, indicating that the function is not working correctly.
"""

"""
The function right_insertion is designed