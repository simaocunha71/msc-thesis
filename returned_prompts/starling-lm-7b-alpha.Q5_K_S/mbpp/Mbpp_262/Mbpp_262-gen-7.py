def split_two_parts(lst, L):
    return lst[:L], lst[L:]


# assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
# print(split_two_parts([1,1,2,3,4,4,5,1],3))


# Time complexity: O(n)
# Space complexity: O(1)




# Python program to illustrate the above approach

# Function to split the list into two parts
def split_two_parts(lst, L):
    # Using list slicing to split the list into two parts
    return lst[:L], lst[L:]

# Driver code
# print(split_two_parts([1,1,2,3,4,4,5,1],3))

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
```
