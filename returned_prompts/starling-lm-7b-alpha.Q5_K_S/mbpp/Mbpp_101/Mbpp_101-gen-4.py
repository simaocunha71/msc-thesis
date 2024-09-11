def kth_element(nums, k):
    sorted_nums = sorted(nums)
    return sorted_nums[k-1]

# assert kth_element([12,3,5,7,19], 2) == 3


# Other Solution
def kth_element(nums, k):
    return sorted(nums)[k-1]
```
    
    
# Python3 Program to get kth Element in Array


# Function to get kth Element in Array
def kth_element(nums, k):

    # Sorting the array
    sorted_nums = sorted(nums)

    # Returning the kth Element
    return sorted_nums[k-1]


# Driver code
nums = [12,3,5,7,19]
k = 2
print(kth_element(nums, k))
```