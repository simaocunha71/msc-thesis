"""
def all_unique(lst):
    seen = set()
    for e in lst:
        if e in seen:
            return False
        seen.add(e)
    return True
"""

def all_unique(lst):
    return len(set(lst)) == len(lst)

# Unit Tests
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False
assert all_unique([]) == True
print("All unit tests passed.")



def all_unique(lst):
    return len(set(lst)) == len(lst)

# Unit Tests
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False
assert all_unique([]) == True
print("All unit tests passed.")



def all_unique(lst):
    return len(set(lst)) == len(lst)

# Unit Tests
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False
assert all_unique([]) == True
print("All unit tests passed.")



def all_unique(lst):
    seen = set()
    for e in lst:
        if e in seen:
            return False
        seen.add(e)
    return True

# Unit Tests
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False
assert all_unique([]) == True
print("All unit tests passed.")



def all_unique(lst):
    return len(set(lst)) == len(lst)

# Unit Tests
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False
assert all_unique([]) == True
print("All unit tests passed.")



def all_unique(lst):
    seen = set()
    for e in lst:
        if e in seen:
            return False
        seen.add(e)
    return True

# Unit Tests
assert all_unique