def count_Occurrence(tup, list_):
    count = 0
    for i in list_:
        count += tup.count(i)
    return count

def test_count_Occurrence():
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3

test_count_Occurrence()





"""
As the problem statement says we need to count the occurrence of all elements of the list in the tuple. So we start by initializing a counter variable to 0. Then we iterate over the elements of the list and for each element, we increment the counter by the number of occurrence of the element in the tuple. Finally we return the counter.

We can test the function by using the assert statement. The assert statement allows us to test if a condition is true or false. If the condition is true then the test passes otherwise the test fails. In this case, we are testing if the function returns the correct result for the given tuple and list.
"""

"""
To solve this problem, you can use the built-in count() function in Python, which returns the number of occurrences of a substring in a string. In this case, you can use the count() function to count the occurrences of each element in the list within the tuple.

Here's an example implementation of the function:

def count_Occurrence(tup, list_):
    count = 0
    for i in list_:
        count += tup.count(i)
    return count

You can test this function by calling it with a tuple and a list as arguments. For example, count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) should return 3, as 'a' and 'b' are present 3 times in the tuple.

To verify the correctness of the function, you can use the assert statement. If the function returns the expected result, the assert statement will not raise an error. Otherwise, an AssertionError will be raised.
"""

"""
To solve this problem, you can use the built-in count() function in Python, which returns the number of occurrences