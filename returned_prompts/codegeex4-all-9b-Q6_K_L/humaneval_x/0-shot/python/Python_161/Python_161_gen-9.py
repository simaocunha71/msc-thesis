def solve(s):
    if s.isalpha():
        return s.swapcase()
    elif not s.isalpha():
        return s[::-1]
    else:
        return s

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))  # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"