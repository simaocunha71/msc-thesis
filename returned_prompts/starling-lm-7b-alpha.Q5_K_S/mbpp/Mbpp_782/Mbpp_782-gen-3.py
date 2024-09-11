def odd_length_sum(arr):
    return sum(sum(arr[i:j+1]) for i in range(len(arr)) for j in range(i,len(arr),2))

odd_length_sum([1,2,4]) # 14

# Time Complexity: O(n^2)
# Space Complexity: O(1)

"""
The above function is using the concept of subarray sum. For each index in the array, we are creating a subarray with that index as the starting index, and creating a subarray with the next index as the ending index.

In the inner loop, we are summing up the elements of the subarray and adding it to the total sum. The outer loop is used to create all possible subarrays with odd lengths.

The time complexity of this function is O(n^2) because for each index in the array, we are creating a subarray with the next index as the ending index. The space complexity of this function is O(1) because we are not using any extra space to store any intermediate values.
"""

"""
To find the sum of all odd length subarrays of an array, you can use the following algorithm:

1. Initialize a variable sum to 0. This variable will store the sum of all odd length subarrays.
2. Iterate over each index i in the array.
3. For each index i, create a subarray with i as the starting index and the next index as the ending index.
4. Calculate the sum of the elements in the subarray and add it to the variable sum.
5. Repeat steps 2-4 for all indices in the array.
6. After iterating over all indices, return the value of the variable sum.

This algorithm has a time complexity of O(n^2) because for each index in the array, we are creating a subarray with the next index as the ending index. The space complexity of this algorithm is O(1) because we are not using any extra space to store any intermediate values.
"""

"""
The above function is a python function that takes an array as input and returns the sum of all odd length subarrays of the array. The function uses a nested loop to iterate over each index in the array and for each index, it