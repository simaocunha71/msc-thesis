```
def find_even_pair(nums):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
    return count
```

# Python3 Solution
```
def find_even_pair(nums):
    return len([i for i in nums for j in nums if (i^j)%2==0])
```

# Python3 Solution
```
def find_even_pair(nums):
    count = 0
    for i in nums:
        for j in nums:
            if (i ^ j) % 2 == 0:
                count += 1
    return count
```

# Python3 Solution
```
def find_even_pair(nums):
    return sum(1 for i in nums for j in nums if (i ^ j) % 2 == 0)
```

# Python3 Solution
```
def find_even_pair(nums):
    return len([i for i in nums for j in nums if (i ^ j) % 2 == 0])
```

# Python3 Solution
```
def find_even_pair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
    return count
```

# Python3 Solution
```
def find_even_pair(nums):
    return sum(1 for i in nums for j in nums if (i ^ j) % 2 == 0)
```

# Python3 Solution
```
def find_even_pair(nums):
    return sum(1 for i in range(len(nums)) for j in range(i + 1, len(nums)) if (nums[i] ^