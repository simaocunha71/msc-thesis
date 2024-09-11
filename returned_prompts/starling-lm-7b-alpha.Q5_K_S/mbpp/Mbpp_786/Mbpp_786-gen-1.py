def right_insertion(arr, value):
    for i in range(len(arr)):
        if arr[i] > value:
            return i
    return len(arr)

# Alternative method using binary search
def right_insertion_binary(arr, value):
    l = 0
    r = len(arr)

    while l < r:
        m = (l + r)//2
        if arr[m] > value:
            r = m
        else:
            l = m + 1
    return l



if __name__ == '__main__':
    arr = [1,2,4,5]
    value = 6
    print(right_insertion(arr, value))
    print(right_insertion_binary(arr, value))


"""
right_insertion([1,2,4,5],6)==4

right_insertion([1,2,4,5],5)==3

right_insertion([1,2,4,5],3)==2

right_insertion([],1)==0

right_insertion([1],1)==0

right_insertion([2],1)==1

right_insertion([1,2],1)==1

right_insertion([2,1],1)==1

right_insertion([1,2,3],1)==2

right_insertion([2,1,3],1)==2

right_insertion([3,2,1],1)==2

right_insertion([1,3,2],1)==2

right_insertion([3,1,2],1)==2

right_insertion([2,3,1],1)==2

right_insertion([3,2,1],1)==2

right_insertion([1,2,3,4],5)==3

right_insertion([1,2,4,5],5)==3

right_insertion([1,2,5,4],5)==2

right_insertion([1,2,4,5],6)==4