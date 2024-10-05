
def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join([char.upper() if char.islower() else char.lower() for char in s])

print(solve("1234"))
print(solve("ab"))
print(solve("#a@C"))
<jupyter_output>
4321
AB
#A@c
<jupyter_text>
Q3: Write a Python program that takes a list of integers and returns True if the sum of two numbers in the list adds up to zero. Otherwise, it should return False. The function should be efficient.
<jupyter_code>
