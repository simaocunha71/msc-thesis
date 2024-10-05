
    def sort_array(array):
        if not array:
            return array
        if len(array) == 1:
            return array
        first = array[0]
        last = array[-1]
        if (first + last) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)

    print(sort_array([]))  # []
    print(sort_array([5]))  # [5]
    print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
    print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1, 0]

"""
Explanation:

In the problem, we are given an array of non-negative integers and we have to sort this array in ascending order if the sum of the first and last elements of the array is odd, or in descending order if it's even. The given array should not be changed.

We can solve this problem by using the sorted() function in Python. This function returns a new sorted list from the elements of any sequence. The sorted() function doesn't change the original list.

In the code, we first handle the edge cases where the array is empty or has only one element. Then we calculate the sum of the first and last elements of the array. If the sum is even, we sort the array in descending order, otherwise we sort it in ascending order.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Given a string, return the string with all characters converted to lowercase and punctuation removed.
<jupyter_code>
