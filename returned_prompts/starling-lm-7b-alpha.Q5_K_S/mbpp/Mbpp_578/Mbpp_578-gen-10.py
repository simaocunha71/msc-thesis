"""
def interleave_lists(*lists):
    new_list = []
    for i in range(len(lists[0])):
        new_list.append(lists[0][i])
        new_list.append(lists[1][i])
        new_list.append(lists[2][i])
    return new_list
"""

def interleave_lists(*lists):
    return [item for sublist in zip(*lists) for item in sublist]


print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))




"""
In this function, we are taking the first list from the parameters and iterating over its length. In each iteration, we add the first element of the first list (lists[0][i]), the first element of the second list (lists[1][i]), and the first element of the third list (lists[2][i]) to the new list. This process is repeated until the end of the lists is reached. Finally, the new list is returned.
"""


"""
In this function, we are using a more efficient approach to interleave the lists. The zip function is used to combine the lists into a single list of tuples, where each tuple contains one element from each of the input lists. We then use a list comprehension to flatten the tuples into a single list. This approach eliminates the need for explicit iteration and concatenation, resulting in a more concise and efficient solution.
"""

"""
In this function, we are using the zip function to combine the input lists into a single list of tuples. Each tuple contains one element from each of the input lists. We then use a list comprehension to flatten the tuples into a single list. This approach eliminates the need for explicit iteration and concatenation, resulting in a more concise and efficient solution.
"""

"""
In this function, we are using the zip function to combine the input lists into a single list of tuples. Each tuple contains one element from each of the input lists. We then use a list