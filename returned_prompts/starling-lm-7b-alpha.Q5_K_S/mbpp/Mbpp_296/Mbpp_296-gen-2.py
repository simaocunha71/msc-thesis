"""
def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count+=1
    return count
"""

def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count+=1
    return count

print(get_Inv_Count([1,20,6,4,5]))

# assert get_Inv_Count([1,20,6,4,5]) == 5
# print(get_Inv_Count([1,20,6,4,5]))
# assert get_Inv_Count([2,2,1,3]) == 3
# print(get_Inv_Count([2,2,1,3]))
# assert get_Inv_Count([3,3,3,3]) == 0
# print(get_Inv_Count([3,3,3,3]))
# assert get_Inv_Count([1,3,5,2,4,6]) == 5
# print(get_Inv_Count([1,3,5,2,4,6]))



"""
In the code above, the function get_Inv_Count() takes an array as an argument and counts the number of inversions in the array. An inversion in an array is a pair of elements (a, b) such that a < b, but appear in the array in the order b, a.

The function uses a nested loop to compare each pair of elements in the array. If the element at index i is greater than the element at index j (where j is greater than i), then an inversion is found and the count is incremented.

After the nested loops finish, the function returns the final count of inversions.

The assert statements at the end of the code are used to test the correctness of the function. Each assert statement compares the output of the function with a known result, and if the two values are not equal, an AssertionError is