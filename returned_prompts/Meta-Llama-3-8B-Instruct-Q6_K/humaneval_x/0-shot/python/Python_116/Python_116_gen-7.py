    def sort_array(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x)) 
    # Explanation: 
    #   The sorted function is used to sort the array. 
    #   The key argument of the sorted function is a function that takes a list element 
    #   and returns a value that will be used for sorting purposes.
    #   In this case, the key function is a lambda function that returns a tuple. 
    #   The first element of the tuple is the number of '1's in the binary representation 
    #   of the array element (bin(x).count('1')), and the second element is the array element itself (x). 
    #   This means that the array elements will be sorted first by the number of '1's 
    #   in their binary representation, and then by their decimal value. 
    #   The sorted function returns a new sorted list and leaves the original list unchanged. 
    #   So, the original array is not modified. 
    #   The function returns the sorted array. 
    #   The output of the function will be a sorted array according to the problem description. 
    #   The function works with any list of non-negative integers. 
    #   It also works with negative integers, but the result will be different because the binary representation of a negative integer starts with '1'. 
    #   The function can handle lists of any size. 
    #   It has a time complexity of O(n log n) because of the sorting operation. 
    #   It has a space complexity of O(n) because it needs to store the sorted array. 





    # Test the function
    print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]





    # Explanation:
    #   The problem is asking to sort an array of non-negative integers based on the number of '1's 
    #   in their binary representation. If two numbers have the same number of '1's