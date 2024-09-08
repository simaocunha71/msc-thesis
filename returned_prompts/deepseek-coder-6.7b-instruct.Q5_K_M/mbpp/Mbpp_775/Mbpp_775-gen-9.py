
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

print(odd_position([2,1,4,3,6,7,6,3]))

"""
Output:
True
"""

Explanation:
The function iterates over the list with step 2, i.e., it starts from the first index and goes to the last with a step of 2. It checks if the number at each odd index is odd, if yes then it returns True else False.
"""

