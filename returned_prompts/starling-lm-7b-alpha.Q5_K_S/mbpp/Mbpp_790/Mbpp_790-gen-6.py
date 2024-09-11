def even_position(input_list):
    if len(input_list) % 2 != 0:
        return False
    else:
        for i in range(0, len(input_list), 2):
            if input_list[i] % 2 != 0:
                return False
    return True


def test_function():
    assert even_position([3, 2, 1]) == False
    assert even_position([3, 2, 2]) == True
    assert even_position([3, 2, 3, 2]) == True
    assert even_position([3, 2, 4, 2]) == True
    assert even_position([3, 2, 2, 5, 2]) == False
    print("All tests passed.")


test_function()

"""
Explanation:
The function even_position takes a list as an input. It first checks if the length of the list is odd. If it is, the function immediately returns False because it is impossible for every even index to contain an even number since there aren't enough even indexes.

If the length of the list is even, the function proceeds to iterate over the list using a for loop. The loop iterates over the list in steps of 2, meaning it only considers the even indexes of the list.

Within the loop, the function checks if the current value at the even index is not even (i.e., it is odd). If it is odd, the function immediately returns False.

If the loop completes without returning False, it means that all even indexes of the list contain even numbers, and the function returns True.
"""

# Python3 program to check if
# all even indexes of a
# given list contains even
# numbers

# Returns True if all
# even indexes of a given
# list contains even numbers
# else False
def even_position(input_list):

    # if length of list is odd
    if len(input_list) % 2 != 0:
        return False

    # Iterate over list in steps of 2
    for i in range(0, len(input_list), 2):

        #