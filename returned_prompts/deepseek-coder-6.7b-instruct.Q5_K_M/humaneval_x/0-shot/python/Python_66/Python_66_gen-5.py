
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
<jupyter_output>
<empty_output>
<jupyter_text>
This function works by iterating over each character in the string. The built-in `ord` function is used to get the ASCII value of the character, and only characters that are uppercase are included in the sum.  Test Cases
<jupyter_code>
print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153
<jupyter_output>
0
131
67
69
131
153
<jupyter_text>
Note: The `isupper()` method returns `True` if all the case-based characters (letters) in the string are uppercase. Else, it returns `False`.  The `ord()` function returns an integer representing the Unicode character.
<jupyter_code>
print(ord('A')) # 65
print(ord('B')) # 66
print(ord('C')) # 67
<jupyter_output>
65
66
67
<jupyter_text>
So in our function, we're summing the ASCII values of uppercase characters 'A' to 'Z'.
<jupyter_code>
print(sum(ord(c) for c in "ABC")) # 198
<jupyter_output>
198
<jupyter_text>
So the sum of the ASCII codes of uppercase characters 'A', 'B', and 'C' is 198.
<jupyter_code>
print(sum(ord(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))