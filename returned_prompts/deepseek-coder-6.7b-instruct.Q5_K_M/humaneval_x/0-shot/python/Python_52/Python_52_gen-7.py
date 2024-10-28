
    for i in l:
        if i >= t:
            return False
    return True

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected: False


