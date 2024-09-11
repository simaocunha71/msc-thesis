"""
def check_K(tuple, k):
    for i in tuple:
        if i == k:
            return True
    return False
"""

def check_K(tuple, k):
    return k in tuple




# assert check_K((10, 4, 5, 6, 8), 6) == True
# assert check_K((10, 4, 5, 6, 8), 7) == False


if __name__ == "__main__":
    tuple = (10, 4, 5, 6, 8)
    k = 6
    print(check_K(tuple, k))
```