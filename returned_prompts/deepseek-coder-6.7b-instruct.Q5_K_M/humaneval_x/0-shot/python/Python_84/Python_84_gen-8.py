
def solve(N):
    return bin(N)[2:]

print(solve(1000))
print(solve(150))
print(solve(147))

"""
bin() function converts the given integer into binary. 
The [2:] is used to get rid of the '0b' that Python prepends to the output of the bin function.
"""
<jupyter_output>
1000
1111010
1001001
<jupyter_text>
Test Case
<jupyter_code>
assert solve(1000) == '1000'
assert solve(150) == '1001010'
assert solve(147) == '1001001'
<jupyter_output>
<empty_output>
<jupyter_text>
All test cases passed successfully.  Solution 2:
<jupyter_code>
def solve(N):
    return bin(N)[2:].zfill(4)

print(solve(1000))
print(solve(150))
print(solve(147))
<jupyter_output>
1000
1001010
1001001
<jupyter_text>
Test Case
<jupyter_code>
assert solve(1000) == '1000'
assert solve(150) == '1001010'
assert solve(147) == '1001001'
<jupyter_output>
<empty_output>
<jupyter_text>
All test cases passed successfully.  Solution 3:
<jupyter_code>
def solve(N):
    return bin(N)[2:].zfill(8)

print(solve(1000))
print(solve(150))
print(solve(147))
<jupyter_output>
1000