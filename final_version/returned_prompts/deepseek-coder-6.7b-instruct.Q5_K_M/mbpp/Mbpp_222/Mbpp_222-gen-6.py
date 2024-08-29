def check_type(tup):
    return len(set(map(type, tup))) == 1

print(check_type((5, 6, 7, 3, 5, 6)))  # True

Explanation:
We use the map function to get a list of the types of all the elements in the tuple. Then we convert that to a set, which removes duplicates, and check if the length of the set is 1. If the length is 1, that means all elements in the tuple are of the same type, and so we return True. Otherwise, we return False.


