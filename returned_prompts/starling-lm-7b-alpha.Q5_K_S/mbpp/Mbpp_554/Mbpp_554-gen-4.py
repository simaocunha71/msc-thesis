def Split(input_list):
    """
    This function takes a list of integers and only returns the odd ones.

    Parameters:
    input_list (list): The list of integers.

    Returns:
    list: The list containing only odd integers.
    """
    # Initialize a result list.
    result = []
    # Iterate over the input list.
    for x in input_list:
        # If the number is odd, add it to the result list.
        if x % 2 != 0:
            result.append(x)
    # Return the result.
    return result

if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):
        def test_split(self):
            self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

        def test_split_2(self):
            self.assertEqual(Split([]), [])

        def test_split_3(self):
            self.assertEqual(Split([1]), [1])

        def test_split_4(self):
            self.assertEqual(Split([2,4,6,8]), [])

    unittest.main()























"""

"""

# ////////////////////////////
# IMPORTS
# ////////////////////////////

# ////////////////////////////
# CONSTANTS AND CONSTANT FUNCTIONS
# ////////////////////////////

# ////////////////////////////
# FUNCTIONS AND METHODS
# ////////////////////////////

def Split(input_list):
    """
    This function takes a list of integers and only returns the odd ones.

    Parameters:
    input_list (list): The list of integers.

    Returns:
    list: The list containing only odd integers.
    """
    # Initialize a result list.
    result = []
    # Iterate over the input list.
    for x in input_list:
        # If the number is odd, add it to the result list.
        if x %