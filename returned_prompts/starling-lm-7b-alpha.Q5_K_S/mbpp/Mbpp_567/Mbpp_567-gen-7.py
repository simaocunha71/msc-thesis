"""
def issort_list(lst):
    """
    Function to check whether a specified list is sorted or not
    Parameters:
        lst: list
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def test_issort_list():
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    print("All Test Passed")
if __name__ == "__main__":
    test_issort_list()
"""

def issort_list(lst):
    """
    Function to check whether a specified list is sorted or not
    Parameters:
        lst: list
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def test_issort_list():
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    print("All Test Passed")
if __name__ == "__main__":
    test_issort_list()



"""
def issort_list(lst):
    """
    Function to check whether a specified list is sorted or not
    Parameters:
        lst: list
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def test_issort_list():
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    print("All Test Passed")
if __name__ == "__main__":
    test_issort_list()
"""


"""
def issort_list(lst