def get_pairs_count(numbers,sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] == sum:
                count += 1
    return count

# Testing
assert get_pairs_count([1,1,1,1],2) == 6
print("All Test Cases Passed")




"""
In the given function, for each index i in the range of the length of the list, it compares the sum of the element at i with all the elements
after i. If the sum of the element at i and the element at j is equal to the given sum, it increments the count variable. It then
returns the final count.
"""

"""
However, the function can be optimized by utilizing Python's dictionary to reduce the time complexity from O(n^2) to O(n).
Here's an improved version of the function:
"""

def get_pairs_count(numbers,sum):
    count = 0
    d = {}
    for num in numbers:
        if sum-num in d:
            count += d[sum-num]
        d[num] = d.get(num,0)+1
    return count

# Testing
assert get_pairs_count([1,1,1,1],2) == 6
print("All Test Cases Passed")


"""
The optimized function first creates a dictionary d to store the occurrence of each number in the list. It then iterates through
the list. For each number, it checks if the difference between the sum and the number is in the dictionary. If it is, it increments the count
by the value in the dictionary. It then updates the dictionary d to store the occurrence of the number. After iterating through the entire list,
it returns the final count.
"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```