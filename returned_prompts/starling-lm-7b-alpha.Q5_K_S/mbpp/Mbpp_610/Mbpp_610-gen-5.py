def remove_kth_element(input_list,k):
    return [x for i,x in enumerate(input_list) if i!=k-1]



"""

def remove_kth_element(input_list,k):
    new_list = []
    for i in range(len(input_list)):
        if i != k-1:
            new_list.append(input_list[i])
    return new_list

"""




















"""
def remove_kth_element(input_list,k):
    new_list = []
    for i in range(len(input_list)):
        if i != k-1:
            new_list.append(input_list[i])
    return new_list

"""


def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]

test_remove_kth_element()

"""



def remove_kth_element(input_list,k):
    return input_list[:k-1] + input_list[k:]

def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]

test_remove_kth_element()

"""

def remove_kth_element(input_list,k):
    new_list = []
    for i in range(len(input_list)):
        if i != k-1:
            new_list.append(input_list[i])
    return new_list

def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 