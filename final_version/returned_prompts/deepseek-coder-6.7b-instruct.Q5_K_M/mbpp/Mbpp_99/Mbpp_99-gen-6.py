
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

print(decimal_to_binary(8))
<jupyter_output>
1000
<jupyter_text>
Problem 3:
<jupyter_code>
