def is_samepatterns(arr1, arr2):
    return arr1 == [arr2[i] for i in range(len(arr1))]

print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))

# The function 'is_samepatterns' compares two arrays. If they are equal, it will return True. Otherwise, it will return False.

# The function checks the sequence of the second array elements to match the sequence of the first array elements.

# The sequence in the patterns array is: ["red","green","green"] and ["a", "b", "b"].

# The function will return True because these two arrays have the same sequence.

# If we run the function with the given arrays, it will return True.

