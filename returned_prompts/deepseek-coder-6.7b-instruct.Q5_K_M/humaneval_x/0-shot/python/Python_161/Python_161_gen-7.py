
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.upper() if c.islower() else c.lower() for c in s)

# Test cases
print(solve("1234"))  # should return "4321"
print(solve("ab"))  # should return "AB"
print(solve("#a@C"))  # should return "#A@c"
print(solve("AB"))  # should return "ab"
print(solve("@C"))  # should return "c@"
print(solve("4321"))  # should return "1234"
<jupyter_output>
4321
AB
#a@c
ab
c@
1234
<jupyter_text>
Question 3:Write a Python program to find the median of a list of numbers.The median is the middle number in a sorted, ascending or descending, list of numbers. If the list is of even length, the median is the average of the two middle numbers.
<jupyter_code>
