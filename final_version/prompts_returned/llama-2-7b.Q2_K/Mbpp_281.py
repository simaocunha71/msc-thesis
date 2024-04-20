"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(l):
    n = len(l) - 1

    def helper(i, j=None):
        """finds out whether the element of index i is unique or not.
            if it is found to be unique, then nothing happens and control comes back to caller of function
            otherwise set the value of j to true and control comes back to the caller again.
            
            If you do not want this functionality add n = len(l) - 1 as a last line in the helper function."""
        if i >= n:
            return True, False
        for k in range(i+1,n):
            if l[k] == l[i]:
                j = True
                print("Lemme tell you that",l[i],"isn't unique yet!")
                break
        
        return helper(j)

    return helper(0)[1]