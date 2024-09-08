
def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(element)
        else:
            if sublist == element:
                count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))  # Output: 3

"""
This function works by iterating over each element in the given list. 
If the element is a sublist, it counts the number of occurrences of the specified element in that sublist. 
If the element is not a sublist, it checks if it is equal to the specified element and increments the count if it is. 
Finally, it returns the total count.
"""
<jupyter_output>
3
<jupyter_text>
3. Write a Python program that accepts a list of integers and returns a dictionary of the counts of unique values in the list. For example, for the input [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], the function should return {1: 1, 2: 2, 3: 3, 4: 4}.
<jupyter_code>
def count_unique_values(lst):
    return {i: lst.count(i) for i in lst}

print(count_unique_values([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
<jupyter_output>
{1: 1, 2: 2, 3: 3, 4: 4}
<jupyter_text>
4. Write a Python program that accepts a string and returns the frequency of each character in the string. For example, for the input "hello", the function should return {'h': 1, '