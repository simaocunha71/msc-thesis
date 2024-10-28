

def change_base(x: int, base: int):
    assert 2 <= base <= 10
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# This function works by dividing the input number by the new base, 
# appending the remainder to the list, and repeating the process until the number is zero.
# Finally, it joins all the digits in the list in reverse order to form a string representation of the number in the new base.
<jupyter_output>
<empty_output>
<jupyter_text>
Task 3: The Collatz ConjectureThe Collatz Conjecture is a mathematical conjecture named after Lothar Collatz, who first proposed it in 1937. The conjecture is defined as follows: Take any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.The following Python code implements the Collatz Conjecture:
<jupyter_code>
def collatz(n: int) -> list[int]:
    """Apply the Collatz Conjecture to the input number n.
    return a list of numbers in the sequence.
    >>> collatz(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    sequence = [n]
    while n != 1:
        if n