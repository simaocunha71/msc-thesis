"""
def check_K(tup, k):
    for i in tup:
        if i == k:
            return True
    return False
"""

def check_K(tup, k):
    return k in tup

# Test
assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((10, 4, 5, 6, 8), 11) == False



# Python3 Program to check
# if an element is present in
# tuple or not

# Function to check if an
# element is present in
# tuple or not
def check_K(tup, k):
    if k in tup:
        return True
    else:
        return False

# Driver Program
if __name__ == "__main__":
    tup = (10, 4, 5, 6, 8)
    k = 6
    print(check_K(tup, k))

    tup = (10, 4, 5, 6, 8)
    k = 11
    print(check_K(tup, k))




































































































































































































































