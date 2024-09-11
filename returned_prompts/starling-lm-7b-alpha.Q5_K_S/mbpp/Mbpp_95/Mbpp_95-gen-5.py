def Find_Min_Length(L):
    # Initialize Min Length
    min_length = len(L[0])

    # Iterate through L
    for l in L:
        # If length of l is smaller than min_length
        if len(l) < min_length:
            # Update min_length
            min_length = len(l)

    # Return min_length
    return min_length

# Test
print(Find_Min_Length([[1],[1,2]])) # 1



"""
The above code works by initializing the minimum length with the length of the first list in the input list. It then iterates through the rest of the lists in the input list, checking if the length of each list is smaller than the current minimum length. If it is, the minimum length is updated to the length of the current list. Finally, the minimum length is returned as the output.
"""

"""
Here's a step-by-step explanation of the code:

1. Initialize the minimum length with the length of the first list in the input list:
   min_length = len(L[0])

2. Iterate through the rest of the lists in the input list:
   for l in L:

3. Check if the length of the current list is smaller than the current minimum length:
   if len(l) < min_length:

4. If it is, update the minimum length to the length of the current list:
   min_length = len(l)

5. After iterating through all the lists in the input list, return the minimum length as the output:
   return min_length
"""

"""
The time complexity of the code is O(n), where n is the total number of elements in the input list. This is because the code iterates through each list in the input list exactly once.

The space complexity of the code is O(1), as the code uses a fixed amount of additional space to store the minimum length.

Overall, the code is an efficient solution to the problem of finding the length of the smallest list in a list of lists.
"""

"""
The code can be easily extended to handle lists of lists of any length, as long as the length of each list is greater