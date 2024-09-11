def left_insertion(arr,val):
    if arr==[]:
        return 0
    if val<arr[0]:
        return 0
    if val>=arr[-1]:
        return len(arr)
    for i in range(len(arr)):
        if val<arr[i]:
            return i
    return len(arr)





"""
def left_insertion(arr,val):
    if arr==[]:
        return 0
    if val<arr[0]:
        return 0
    if val>=arr[-1]:
        return len(arr)
    for i in range(len(arr)):
        if val<arr[i]:
            return i
    return len(arr)
"""

def test_left_insertion():
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,4,5],1)==0
    assert left_insertion([1,2,4,5],3)==2
    assert left_insertion([],5)==0
    assert left_insertion([1],5)==0
    assert left_insertion([5],1)==1
    assert left_insertion([5,1],2)==1

test_left_insertion()


"""
def left_insertion(arr,val):
    if arr==[]:
        return 0
    if val<arr[0]:
        return 0
    if val>=arr[-1]:
        return len(arr)
    for i in range(len(arr)):
        if val<arr[i]:
            return i
    return len(arr)
"""

def test_left_insertion():
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,4,5],1)==0
    assert left_insertion([1,2,4,5],3)==2
    assert left_insertion([],5)==0
    assert left_insertion([1],5)==0
    assert left_insertion([5],1)==