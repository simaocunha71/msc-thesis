"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

def flatten_list(l):
    """Flatten a nested list structure
        Args:
            l (list) [nested list structure] -> [the final result]
        Return:
            None
        """
    for item in l:
        if type(item) == type([]) or len(l[0]) == 1:
            flatten_list(item)
        else:
            print("Inside nested list")
            print(type(l))
        break
    return l