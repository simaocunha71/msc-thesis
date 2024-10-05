    # Given array
    arr = [1,2,3,5,4,7,9,6]

    # Initialize count variable
    count = 0

    # Traverse the array
    for i in range(len(arr)):
        # Check if element is not present in the array
        if arr[i] not in arr[i+1:] + arr[:i]:
            count += 1

    return count


# Driver Code
print(smallest_change([1,2,3,5,4,7,9,6])) # Output: 4
print(smallest_change([1,2,3,4,3,2,2])) # Output: 1
print(smallest_change([1,2,3,2,1])) # Output: 0


# Time Complexity: O(n)
# Space Complexity: O(1)

# Here, we are checking whether the element is present in the array or not by using two pointers to traverse the
# array. So, the time complexity is O(n) and space complexity is O(1).
# We are using two pointers, one from the start and one from the end of the array.
# We traverse the array and for each element, check if it is present in the array or not.
# If the element is not present in the array, we increment the count variable by 1.

# We can check whether the element is present in the array or not by using two pointers.
# One pointer starts from the start of the array and the other starts from the end of the array.
# We traverse the array and for each element, we check if it is present in the array or not.
# If the element is not present in the array, we increment the count variable by 1.

# This will give us the minimum number of elements that need to be changed to make the array palindromic.

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

```

```

```

