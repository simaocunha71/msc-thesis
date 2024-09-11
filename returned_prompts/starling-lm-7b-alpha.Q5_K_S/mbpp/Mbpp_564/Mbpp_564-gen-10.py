def count_Pairs(a,b):
    count=0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]!=b[j]:
                count+=1
    return count

# Driver Code
print(count_Pairs([1,2,1],3))






"""
O(n^2)
"""

"""
Explanation
Here, in the function count_Pairs, we are iterating over the list 'a' and then for each element of 'a', we are checking whether it is equal to any element of 'b' or not. If it is not equal, we are incrementing the count by 1.
Now, the time complexity of this function is O(n^2) because we are iterating over the two lists 'a' and 'b' and for each iteration, we are comparing each element of 'a' with each element of 'b'.

"""

"""
This function will count the number of possible unordered pairs where both elements are unequal.
For example, if the input is [1,2,1], then the output should be 2 because we have 2 possible pairs {1,2} and {2,1}.
"""

"""
To solve this problem, we can use nested loops. We can iterate over the list 'a' and for each element of 'a', we can iterate over the list 'b'. If the current elements of 'a' and 'b' are not equal, we can increment the count by 1.
Finally, we return the count.
"""

"""
The time complexity of this solution is O(n^2) because we are iterating over the two lists 'a' and 'b' and for each iteration, we are comparing each element of 'a' with each element of 'b'.
The space complexity is O(1) because we are not using any extra space."""


# Python3 program to find number of unordered pairs

"""
This code is contributed by 29AjayKumar
"""

"""
In this Python program, we are defining a function called count_Pairs which takes two lists, 'a' and 'b', as input. Inside the function, we initialize