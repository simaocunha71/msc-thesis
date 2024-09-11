def div_list(l1,l2):
    div_list = []
    for i in range(len(l1)):
        div_list.append(l1[i]/l2[i])
    return div_list

from nose.tools import assert_equal
def test_div_list():
    assert_equal(div_list([4,5,6],[1, 2, 3]),[4.0,2.5,2.0])

test_div_list()

"""
In the above code, we have created a function div_list which takes two lists as an argument and divides each element of the first list by the corresponding element in the second list. The function returns a new list where the division is performed. We have used a for loop to iterate through the length of the lists. For each index in the range of the length of the lists, we divide the element at that index of the first list by the element at the same index of the second list and append the result to the div_list. Finally, we return the div_list. To test the function, we have written a test_div_list function which asserts that the div_list function returns the expected result for the given test case.
"""

"""
In the above code, we have created a function div_list which takes two lists as an argument and divides each element of the first list by the corresponding element in the second list. The function returns a new list where the division is performed. We have used a for loop to iterate through the length of the lists. For each index in the range of the length of the lists, we divide the element at that index of the first list by the element at the same index of the second list and append the result to the div_list. Finally, we return the div_list. To test the function, we have written a test_div_list function which asserts that the div_list function returns the expected result for the given test case.
"""

"""
In the above code, we have created a function div_list which takes two lists as an argument and divides each element of the first list by the corresponding element in the second list. The function returns a new list where the division is performed. We have used a for loop to iterate through the length of the lists. For each index in