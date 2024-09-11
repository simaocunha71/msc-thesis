"""
def count_Pairs(lst,n):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] != lst[j] and lst[i] != n and lst[j] != n:
                count += 1
    return count

# Driver Code
print(count_Pairs([1,2,1],3))
"""

# Here's a step by step breakdown of the above code:

# 1. The function count_Pairs takes two parameters: lst (the list of integers) and n (an integer from the list).

# 2. It initializes a variable count to keep track of the number of unordered pairs with unequal elements.

# 3. It uses a nested loop to compare each element in the list with every other element. The outer loop iterates over the indices of the list, and the inner loop iterates over the indices of the list starting from the current outer loop index.

# 4. Inside the nested loop, it checks if the current pair of elements (lst[i] and lst[j]) are unequal and not equal to n. If both conditions are true, it increments the count variable by 1.

# 5. After the nested loop finishes, the function returns the final count of unordered pairs with unequal elements.

# 6. The driver code calls the function with the list [1,2,1] and the integer 3, and prints the result (which should be 2 in this case).

# This code will count the number of possible unordered pairs where both elements are unequal, and return the result.
"""

def count_Pairs(lst,n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and lst[i] != n and lst[j] != n:
                count += 1
    return count

# Driver Code
print(count_Pairs([1,2,1],3))
"""

In this code, the function count_Pairs takes