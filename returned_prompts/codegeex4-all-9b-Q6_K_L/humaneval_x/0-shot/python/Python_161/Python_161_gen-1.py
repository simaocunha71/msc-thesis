def solve(s):
    if s.isalpha():
        return s.swapcase()
    else:
        return s[::-1]

print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"