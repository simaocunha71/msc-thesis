"""
def count_samepair(list1,list2,list3):
    same_pair_count = 0
    for i in range(0,len(list1)):
        if list1[i] == list2[i] == list3[i]:
            same_pair_count += 1
    return same_pair_count
"""

def count_samepair(list1,list2,list3):
    same_pair_count = 0
    for i in range(0,len(list1)):
        if list1[i] == list2[i] == list3[i]:
            same_pair_count += 1
    return same_pair_count

# assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
# print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))


def count_samepair_test():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    print("All tests passed.")

count_samepair_test()


"""
