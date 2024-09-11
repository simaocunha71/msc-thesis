def kth_element(arr, k):
    arr.sort()
    return arr[k-1]


# Driver Code
print(kth_element([12,3,5,7,19], 2))





"""
Explanation:
The function kth_element takes in two parameters: an array, arr, and an integer, k. Inside the function, the array is sorted in ascending order using the sort() method. Then, the kth element is returned by indexing into the sorted array with the value of k minus one (since 1-based indexing is used). This means that the kth smallest element in the array will be the kth element in the sorted array.

In the provided example, the function is called with the array [12,3,5,7,19] and k = 2. The array is sorted to become [3,5,7,12,19]. Since k is 2, the 2nd smallest element in the array is 5, and this is the value that is returned by the function.
"""

"""
Explanation:
In the provided example, the function kth_element is called with the array [12,3,5,7,19] and k = 2. The array is sorted to become [3,5,7,12,19]. Since k is 2, the 2nd smallest element in the array is 5, and this is the value that is returned by the function.

The function works by first sorting the array in ascending order using the sort() method. This allows us to find the kth smallest element in the array by indexing into the sorted array with the value of k minus one (since 1-based indexing is used). In the example, the 2nd smallest element in the sorted array is 5, which is the value that is returned by the function.
"""





"""
Explanation:
The function kth_element takes in two parameters: an array, arr, and an integer, k. Inside the function, the array is sorted in ascending order using the sort() method. Then, the kth element is returned by indexing into the sorted array with the value of k minus one (since 