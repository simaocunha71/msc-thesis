def find_Odd_Pair(arr,n):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) & 1:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))


"""
Explanation:
In the given array, we have (5,4),(5,7),(5,2),(5,1),(4,7),(4,2),(4,1),(7,2),(7,1),(2,1) these are 10 pairs. 
If we XOR these pairs then, 
5^4=1, 5^7=2, 5^2=7, 5^1=4, 4^7=1, 4^2=6, 4^1=5, 7^2=5, 7^1=6, 2^1=3.
Out of these only 6 pairs have odd XOR values i.e., 1,2,5,1,6,3. 
So, the function returns 6.
"""


"""
Complexity Analysis:
Time Complexity: O(n^2) as there are two nested loops traversing the array.
Space Complexity: O(1) as no extra space is used.
"""


"""
This approach is not efficient for large inputs because the time complexity is O(n^2). 
A better approach would be to use a hash table or sort the array first and then iterate through it to find the pairs.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
