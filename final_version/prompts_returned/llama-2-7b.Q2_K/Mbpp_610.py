"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""

def remove_kth_element(list, k):
    if list == []:
        return []

    else:
         for index in range(0,len(list)):
             print("current element is ", list[index])
             if index != k - 1 and index %2==1:
                pass
             elif index == k-1:
                  return remove_kth_element([k] + list[index+1:],k)    
         return remove_kth_element(list[index+1:],k)