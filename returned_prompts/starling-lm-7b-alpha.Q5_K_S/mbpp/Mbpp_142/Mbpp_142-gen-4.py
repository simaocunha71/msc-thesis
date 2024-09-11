"""
def count_samepair(list_one,list_two,list_three):
    count=0
    for i in range(len(list_one)):
        if list_one[i]==list_two[i]==list_three[i]:
            count+=1
    return count


def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3

test_count_samepair()

"""

def count_samepair(list_one, list_two, list_three):
    """
    Write a function to count number items that are identical in the same position of three given lists.

    Args:
        list_one: A list of integers
        list_two: A list of integers
        list_three: A list of integers

    Returns:
        The number of items that are identical in the same position of three given lists.
    """
    count = 0
    for i in range(len(list_one)):
        if list_one[i] == list_two[i] == list_three[i]:
            count += 1
    return count


def test_count_samepair():
    assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3


test_count_samepair()































































































