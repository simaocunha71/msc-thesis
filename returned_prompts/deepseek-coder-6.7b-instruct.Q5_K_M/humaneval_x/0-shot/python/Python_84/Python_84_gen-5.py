
def solve(N):
    return bin(N)[2:].replace("0b", "").replace("0", "").replace("1", "2").replace("2", "1")


print(solve(1000))
print(solve(150))
print(solve(147))

# The solution is to first convert the number to binary, remove the "0b" from the start, replace all zeros with twos, and then replace all twos with ones. This effectively reverses the binary representation.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
