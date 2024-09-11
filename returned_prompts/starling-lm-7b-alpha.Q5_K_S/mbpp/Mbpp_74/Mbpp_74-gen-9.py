def is_samepatterns(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

# assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True

# assert is_samepatterns(["red","green","blue"], ["a", "b", "c"])==False

# assert is_samepatterns(["red","green","blue"], ["c", "b", "a"])==False

# assert is_samepatterns(["green"], ["green"])==True

# assert is_samepatterns(["green"], ["blue"])==False

# assert is_samepatterns(["red"], ["blue"])==False

# assert is_samepatterns([], [])==True

# assert is_samepatterns(["red"], [])==False

# assert is_samepatterns([], ["blue"])==False

# assert is_samepatterns(["red"], ["red"])==True

# assert is_samepatterns(["red","green"], ["green","red"])==True

# assert is_samepatterns(["red","green"], ["red","blue"])==False

"""
Test cases:

is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
is_samepatterns(["red","green","blue"], ["a", "b", "c"])==False
is_samepatterns(["red","green","blue"], ["c", "b", "a"])==False
is_samepatterns(["green"], ["green"])==True
is_samepatterns(["green"], ["blue"])==False
is_samepatterns(["red"], ["blue"])==False
is_samepatterns([], [])==True
is_samepatterns(["red"], [])==False
is_samepatterns([], ["blue"])==False
is_samepatterns(["red"], ["red"])==True
is_samepatterns(["red","green"], ["green","red"])