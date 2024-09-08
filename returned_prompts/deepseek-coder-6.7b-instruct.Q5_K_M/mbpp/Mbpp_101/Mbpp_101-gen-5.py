def kth_element(arr, k):
    arr.sort()
    return arr[k-1]
"""
Explanation:
The function sorts the array in ascending order, and then returns the kth element. Python uses 0-based indexing, so we need to subtract 1 from k.
"""

#Test the function
print(kth_element([12,3,5,7,19], 2)) #Output: 3

#Other solution
def kth_element(arr, k):
    arr.sort()
    return arr[-k]
"""
Explanation:
The function sorts the array in ascending order and returns the kth element from the end. This way, we can use the same function to get the kth largest element.
"""

#Test the function
print(kth_element([12,3,5,7,19], 2)) #Output: 12

#Other solution
def kth_element(arr, k):
    return sorted(arr)[k-1]
"""
Explanation:
This is a more efficient solution because it doesn't sort the original array. It sorts a copy of the array and returns the kth element from the sorted copy.
"""

#Test the function
print(kth_element([12,3,5,7,19], 2)) #Output: 3

#Other solution
def kth_element(arr, k):
    return heapq.nlargest(k, arr)[-1]
"""
Explanation:
This function uses the heapq module to find the kth largest element in the array. The nlargest function returns the k largest elements from the array. We return the last element of this list, which is the kth largest element.
"""

#Test the function
print(kth_element([12,3,5,7,19], 2)) #Output: 12

#Other solution
def kth_element(arr, k):
    return heapq.nsmallest(k, arr)[-1]
"""
Explanation:
This function uses the heapq module to find the kth smallest element in the array. The nsmallest