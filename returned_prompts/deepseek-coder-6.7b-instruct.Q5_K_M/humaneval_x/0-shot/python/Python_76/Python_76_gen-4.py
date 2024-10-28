
    def is_simple_power(x, n):
        if n < 1 or x < 1:
            return False
        while x > 1:
            x = x / n
            if x != int(x):
                return False
        return True

print(is_simple_power(1, 4)) # => True
print(is_simple_power(2, 2)) # => True
print(is_simple_power(8, 2)) # => True
print(is_simple_power(3, 2)) # => False
print(is_simple_power(3, 1)) # => False
print(is_simple_power(5, 3)) # => False
print(is_simple_power(64, 2)) # => True

The function works by dividing the input number x by the base n, and checking if the result is an integer. This is done in a loop until x becomes 1. If at any point the result is not an integer, the function returns False. If the loop completes without finding a non-integer result, the function returns True, indicating that the input number is a simple power of the base.
<jupyter_output>
<empty_output>
<jupyter_text>
