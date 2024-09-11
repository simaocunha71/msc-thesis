"""
def count_samepair(lst1,lst2,lst3):
    samepair = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            samepair += 1
    return samepair

def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    print("All tests passed")

test_count_samepair()
"""

def count_samepair(lst1,lst2,lst3):
    samepair = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            samepair += 1
    return samepair

def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    print("All tests passed")

test_count_samepair()



# Created by : Venkat
# Date : 27-09-2020
# Purpose : Python Practice
# Source : Python Practice



"""
Here is a Python function that counts the number of items that are identical in the same position of three given lists.

The function takes three lists as input and returns an integer representing the number of items that are identical in the same position of the three lists.

Here are some sample inputs and outputs of the function.

count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3

The