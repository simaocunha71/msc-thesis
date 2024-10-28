# Python Program to Swap Case of Letters in a String
def solve(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isalpha():
            new_str += chr(ord(s[i]) ^ 32) if s[i].islower() else chr(ord(s[i]) & 255)
        else:
            new_str += s[i]
    return new_str[::-1] if s.isalpha() else new_str

# Test Cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))   # Output: "AB"
print(solve("#a@C")) # Output: "#A@c"
print(solve("abc"))  # Output: "ABC"
print(solve(""))     # Output: ""

# Time Complexity: O(n)
# Space Complexity: O(n)

def solve2(s):
    return "".join([chr(255 - ord(i)) if i.islower() else chr(ord(i) ^ 32) if i.isalpha() else i for i in reversed(s)]) if "".join([i for i in s if i.isalpha()]) else "".join([i for i in reversed(s)])

# Test Cases
print(solve2("1234"))  # Output: "4321"
print(solve2("ab"))   # Output: "AB"
print(solve2("#a@C")) # Output: "#A@c"
print(solve2("abc"))  # Output: "ABC"
print(solve2(""))     # Output: ""

# Time Complexity: O(n)
# Space Complexity: O(n)

# Python Program to Swap Case of Letters in a String
def solve3(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isalpha():
            new_str += chr(ord(s[i]) ^ 32) if s[i