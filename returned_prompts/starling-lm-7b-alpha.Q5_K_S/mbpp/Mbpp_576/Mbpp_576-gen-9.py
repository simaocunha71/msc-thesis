def is_Sub_Array(list1,list2):
    if len(list1) > len(list2):
        return is_Sub_Array(list2,list1)
    for i in range(len(list2)-len(list1)+1):
        if list1 == list2[i:i+len(list1)]:
            return True
    return False

# Test
print(is_Sub_Array([1,4,3,5],[1,2]))  # False
print(is_Sub_Array([1,4,3,5],[1,4,3,5,6]))  # True


# Other Solution
def is_Sub_Array(list1, list2):
    if list1 == []:
        return True
    if len(list1) > len(list2):
        return False
    if list1[0] == list2[0]:
        return is_Sub_Array(list1[1:], list2[1:])
    else:
        return is_Sub_Array(list1, list2[1:])

print(is_Sub_Array([1,4,3,5],[1,2]))  # False
print(is_Sub_Array([1,4,3,5],[1,4,3,5,6]))  # True

"""
The function first checks if the length of the first array is greater than the second array. If so, the function returns the result of calling itself with the second array as the first array and the first array as the second array. This is because if the first array is not a subarray of the second array, then the second array cannot be a subarray of the first array. 

Next, the function checks if the length of the first array is less than or equal to the length of the second array. If so, it checks if the first element of the first array is equal to the first element of the second array. If so, the function recursively calls itself with the second element of the first array and the second element of the second array as the first and second arrays, respectively. 

If the first element of the first array is not equal to the first element of the second array, the function recursively calls itself with the first element