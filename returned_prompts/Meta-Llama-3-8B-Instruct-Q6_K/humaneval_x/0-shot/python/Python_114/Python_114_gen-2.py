    # Initialize the minimum sum as infinity
    min_sum = float('inf')
    # Initialize the current sum as 0
    current_sum = 0
    # Initialize the left pointer as 0
    left = 0
    # Iterate over the array
    for right in range(len(nums)):
        # Add the current element to the current sum
        current_sum += nums[right]
        # While the current sum is greater than or equal to 1
        while current_sum >= 1:
            # Update the minimum sum
            min_sum = min(min_sum, current_sum)
            # Subtract the leftmost element from the current sum
            current_sum -= nums[left]
            # Move the left pointer to the right
            left += 1
    # Return the minimum sum
    return min_sum

B:

def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        if current_sum < 1:
            continue
        
        while current_sum >= 1:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[i]
            i += 1
    
    return min_sum

C:

def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        while current_sum >= 1:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[i]
    
    return min_sum

D:

def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    left = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= 1:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[left]
            left += 1
    
    return min_sum

E:

def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    left = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= 1:
            min_sum =