def is_perfect_square(n):
    return n == (int(n**0.5))**2

assert not is_perfect_square(10)

# Another solution using math library
import math

def is_perfect_square(n):
    return math.isqrt(n)**2 == n

assert not is_perfect_square(10)

# Another solution using math library
import math

def is_perfect_square(n):
    return math.sqrt(n).is_integer()

assert not is_perfect_square(10)


# Another solution using math library
import math

def is_perfect_square(n):
    return n in [i*i for i in range(int(math.sqrt(n))+1)]

assert not is_perfect_square(10)
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2**
<jupyter_code>
