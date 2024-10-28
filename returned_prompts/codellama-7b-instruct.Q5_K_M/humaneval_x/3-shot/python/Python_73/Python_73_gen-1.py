    # We need to find the minimum number of elements that need to be changed.
    # The minimum number of elements that need to be changed will be the minimum number
    # of elements that need to be changed to make the array a palindrome.
    #
    # We can find the minimum number of elements that need to be changed by comparing
    # the number of elements in the array with the number of elements in the palindrome of the array.
    #
    # A palindrome of an array is an array that is read the same backwards and forwards.
    #
    # For example, if the input array is [1, 2, 3, 4, 5, 6, 7], a palindrome of this array is [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1].
    #
    # We can find the length of the palindrome of an array by finding the length of the array and then subtracting 1.
    # For example, if the input array is [1, 2, 3, 4, 5, 6, 7], the length of the palindrome of this array is 12 - 1 = 11.
    #
    # We can then find the minimum number of elements that need to be changed to make the array a palindrome
    # by comparing the length of the array with the length of the palindrome of the array.
    #
    # For example, if the input array is [1, 2, 3, 4, 5, 6, 7], the minimum number of elements that need to be changed
    # is 11 - 7 = 4.
    #
    # Therefore, we return 4.
    #
    # Complexity:
    #
    # Time: O(n), where n is the length of the input array
    # Space: O(1)
    #
    # The time complexity is O(n) because we are iterating over the array once.
    #
    # The space complexity is O(1) because we are only using constant space.


    # We need to find the minimum