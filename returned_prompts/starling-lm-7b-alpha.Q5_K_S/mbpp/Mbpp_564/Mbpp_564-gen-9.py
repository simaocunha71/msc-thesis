def count_Pairs(arr,n):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]!=arr[j]):
                count+=1
    return count

# Driver code
arr = [1, 2, 1]
n = len(arr)
print(count_Pairs(arr,n))

# This code is contributed by Rishabh Singh



# Time complexity O(n^2)
"""
Explanation:
The time complexity of this solution is O(n^2). As we need to compare every element with every other element in the array, which takes O(n) time for each element.
"""

"""
The space complexity of this solution is O(1). As the space used is constant, independent of the size of the input array. We are not using any additional data structures.
"""

"""
The above solution has a time complexity of O(n^2) and a space complexity of O(1).
"""


# Python3 program to count all unordered
# pairs of unequal elements

# Function to count all unordered pairs
# of unequal elements
def countPairs(arr, n):

    # Initialize result
    count = 0;

    # Count all unordered pairs
    # of unequal elements
    for i in range(n):
        for j in range(i + 1, n):

            # If both elements are unequal
            if (arr[i] != arr[j]):
                count += 1;

    return count

# Driver program
arr = [1, 2, 1]
n = len(arr)
print(countPairs(arr, n))

# This code is contributed by Rishabh Singh

"""
Explanation:
The time complexity of this solution is O(n^2). As we need to compare every element with every other element in the array, which takes O(n) time for each element.
"""

"""
The space complexity of this solution is O(1). As the space used is constant, independent of the size of the input array. We are