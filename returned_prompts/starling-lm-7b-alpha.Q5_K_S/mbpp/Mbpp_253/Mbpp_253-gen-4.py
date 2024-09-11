def count_integer(input_list):
    result = 0
    for element in input_list:
        if isinstance(element, int):
            result += 1
    return result

count_integer([1,2,'abc',1.2])


# Another approach using list comprehension
def count_integer(input_list):
    return len([i for i in input_list if isinstance(i, int)])

count_integer([1,2,'abc',1.2])


# Yet another approach using filter()
def count_integer(input_list):
    return len(filter(lambda x: isinstance(x, int), input_list))

count_integer([1,2,'abc',1.2])


"""
The first function works by iterating over the input list and incrementing the result by 1 each time it encounters an integer. It uses the isinstance() function to check if an element is an integer.

The second function works by using list comprehension to create a new list containing only the integers in the input list. It then uses the len() function to find the length of this new list, which is the number of integers in the input list.

The third function works by using the filter() function to create a new list containing only the integers in the input list. It then uses the len() function to find the length of this new list, which is the number of integers in the input list. The filter() function uses a lambda function to specify the condition that an element must be an integer to be included in the new list.
"""



"""
In this code, the function count_integer() takes a list as an argument and returns the number of integer elements in the list. It does this by using a for loop to iterate over each element in the list. Inside the loop, it uses the isinstance() function to check if the element is an integer. If it is, it increments a counter variable, result, by 1. Finally, it returns the value of result, which is the number of integer elements in the list.
"""


"""
The function count_integer() uses a for loop to iterate over each element in the input_list. It then uses the isinstance() function to check if each element is an integer. If it is,