def test_duplicate(arr):
    return len(arr) != len(set(arr))

print(test_duplicate([1,2,3,4,5])) # False

# Alternative solution
def test_duplicate_alt(arr):
    return any(arr.count(i) > 1 for i in arr)

print(test_duplicate_alt([1,2,3,4,5])) # False

# Another alternative solution
def test_duplicate_alt2(arr):
    return len(arr) != len(arr)

print(test_duplicate_alt2([1,2,3,4,5])) # False

# Yet another alternative solution
def test_duplicate_alt3(arr):
    return sum(arr.count(i) > 1 for i in arr)

print(test_duplicate_alt3([1,2,3,4,5])) # 0
"""
This solution checks if the sum of the duplicate counts (if there are any) is greater than 0.
If there are no duplicates, it will return 0.
"""
<jupyter_output>
False
False
False
0
<jupyter_text>
Exercise 2
<jupyter_code>
