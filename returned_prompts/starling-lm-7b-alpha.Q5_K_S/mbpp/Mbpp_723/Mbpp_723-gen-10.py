def count_same_pair(list_1,list_2):
    count = 0
    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            count += 1
    return count






























"""
Correct Solution:
"""
def count_same_pair(list_1,list_2):
    count = 0
    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            count += 1
    return count

def test_count_same_pair():
    assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
    assert count_same_pair([1, 2, 3, 4, 5],[2, 2, 3, 1, 2, 6, 7, 9])==3
    assert count_same_pair([1, 2, 3, 4, 5],[1, 2, 3, 4, 5])==5
    print("All tests passed!")

test_count_same_pair()


```
