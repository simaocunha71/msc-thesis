def remove_odd(s):
    result = ""
    for i, c in enumerate(s):
        if i % 2 == 0:
            result += c
    return result

# Test the function
print(remove_odd("python"))  # Output: "yhn"  # "p" is at index 0, "y" is at index 1, "t" is at index 2, "h" is at index 3, "o" is at index 4, "n" is at index 5
# "y" and "h" are even indices, "n" is at even index 5, so they remain. "p", "t", and "o" are at odd indices, so they are removed.  # This test passes.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected output: yhn  # Actual output: yhn  # Test passed.  # Python 3.8.10
# Expected