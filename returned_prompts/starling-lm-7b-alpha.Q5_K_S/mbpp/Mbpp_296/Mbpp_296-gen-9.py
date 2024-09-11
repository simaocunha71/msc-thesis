"""
def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count

"""

def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count


def test_get_Inv_Count():
    assert get_Inv_Count([1,20,6,4,5]) == 5

test_get_Inv_Count()


"""

def test_get_Inv_Count():
    assert get_Inv_Count([1,20,6,4,5]) == 5



def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count


def test_get_Inv_Count():
    assert get_Inv_Count([1,20,6,4,5]) == 5

test_get_Inv_Count()


def get_Inv_Count(arr):
    def merge_sort(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left,right)

    def merge(left,right):
        res = []
        i,j = 0,0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
                count += (len(left)-i)
