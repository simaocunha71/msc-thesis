def count_samepair(list1,list2,list3):
    count=0
    for i in range(len(list1)):
        if list1[i]==list2[i]==list3[i]:
            count+=1
    return count

"""
def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    print("All tests passed.")
test_count_samepair()
"""

#Alternate Solution
def count_samepair(list1,list2,list3):
    return sum(1 for i in zip(list1,list2,list3) if i[0]==i[1]==i[2])

"""
def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    print("All tests passed.")
test_count_samepair()
"""

#Alternate Solution
def count_samepair(list1,list2,list3):
    return sum(len(set(i[0],i[1],i[2]))<3 for i in zip(list1,list2,list3))

"""
def test_count_samepair():
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    print("All tests passed.")
test_count_samepair()
"""

#Alternate Solution
def count_samepair(list1,list2,list3):
    return sum(1 for i in zip(list1,list2,list3) if i[0]==i[1]==i[2])

"""
def