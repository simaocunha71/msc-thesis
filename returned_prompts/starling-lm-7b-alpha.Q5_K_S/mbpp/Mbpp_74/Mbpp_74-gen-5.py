def is_samepatterns(pattern1, pattern2):
    n1 = len(pattern1)
    n2 = len(pattern2)
    if n1 != n2:
        return False
    for i in range(n1):
        if pattern1[i] != pattern2[i]:
            return False
    return True

# Test
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
print("Test Passed")

# Test
assert is_samepatterns(["red","green","green"], ["a", "c", "c"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red","green","blue"], ["a", "b", "c"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red","green","blue"], ["c", "b", "a"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red","green","blue"], ["a", "b", "c"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red","blue"], ["a", "b"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["a"])==True
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["a", "c"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["b", "c"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["b"])==True
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["a"])==True
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["red"])==True
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["green"])==False
print("Test Passed")

# Test
assert is_samepatterns(["red"], ["blue"])==False
print