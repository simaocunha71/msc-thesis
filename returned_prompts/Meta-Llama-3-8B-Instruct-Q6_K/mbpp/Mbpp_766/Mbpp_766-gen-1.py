def pair_wise(lst):
    result = []
    for i in range(len(lst)):
        if i < len(lst) - 1:
            result.append((lst[i], lst[i+1]))
    return result

# Test case:
print(pair_wise([1,1,2,3,3,4,4,5]))
# Expected output: [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]


# Explanation:
This function takes a list as input and returns a list of pairs of consecutive items in the list. It does this by iterating over the list and appending each pair of consecutive items to the result list. The condition `if i < len(lst) - 1:` ensures that the last element of the list is not paired with anything, as there is no next element. The function then returns the list of pairs. The test case provided shows that the function works correctly for a list with duplicate elements. 

# Improvement:
The function can be improved by using list comprehension, which is more concise and readable. Here is the improved version:

def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]


This version of the function does the same thing as the original, but is more concise and easier to read. It uses a list comprehension to create the list of pairs, and the condition `range(len(lst)-1)` ensures that the last element is not paired with anything. 

# Edge cases:
The function works correctly for lists with any number of elements, including empty lists and lists with a single element. For an empty list, the function returns an empty list. For a list with a single element, the function returns an empty list. 

However, the function may not work correctly for lists with non-iterable elements, such as strings or dictionaries. This is because the function assumes that the elements of the list are all iterable (i.e., they can be iterated over using a for loop). If the list contains non-iterable elements, the function may raise an error. 

To handle this edge case, the function could be modified to check if each element is iterable before trying to iterate over it. This would ensure that the function works correctly even for lists with non-iterable elements. 

For example, the improved version of the function could be modified as