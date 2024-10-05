
    # Initialize an empty dictionary
    num_dict = {}

    # For each number in the list
    for num in l:

        # If the opposite of the number is in the dictionary
        if -num in num_dict:

            # Return True
            return True

        # If the number is not in the dictionary
        else:

            # Add the number to the dictionary
            num_dict[num] = num

    # After checking all the numbers, if no pairs sum to zero, return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# Complexity Analysis
# The time complexity of this function is O(n), where n is the length of the list.
# This is because we are looping through the list only once.
# The space complexity is also O(n), because in the worst case scenario (when all elements are distinct), we are storing all the elements in the dictionary.
# In the best case scenario (when all elements sum to zero), we are storing half the list in the dictionary.
# Thus, the space complexity is O(n/2) = O(n), which is the same as the time complexity.
<jupyter_output>
<empty_output>
<jupyter_text>
