def check_K(tup, k):
    if k in tup:
        return True
    else:
        return False

print(check_K((10, 4, 5, 6, 8), 6))  # True
print(check_K((10, 4, 5, 6, 8), 9))  # False



"""
