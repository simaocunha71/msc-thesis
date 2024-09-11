def is_nonagonal(n):
    return True if n % 7 == 0 else False

def nonagonal(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * (7 * i - 1)
    return sum


def nonagonal_nth(n):
    if is_nonagonal(n) == False:
        print("The number is not a nonagonal number")
    else:
        print(nonagonal(n))


if __name__ == '__main__':
    nonagonal_nth(10)


"""
The nth nonagonal number is the sum of the first n positive integers each multiplied by 7i−1 where i is the index.
"""

"""
The first few nonagonal numbers are:

    1 = 1 × (7 × 1 − 1)
    7 = 1 × (7 × 2 − 1) + 2 × (7 × 2 − 1)
   24 = 1 × (7 × 3 − 1) + 2 × (7 × 3 − 1) + 3 × (7 × 3 − 1)
  127 = 1 × (7 × 4 − 1) + 2 × (7 × 4 − 1) + 3 × (7 × 4 − 1) + 4 × (7 × 4 − 1)
  ...

We can see that the nth nonagonal number is the sum of the first n positive integers each multiplied by 7i−1 where i is the index.
"""


"""
To check if a number is a nonagonal number, we can simply check if it is divisible by 7, since all nonagonal numbers are divisible by 7.
"""


"""
To find the nth nonagonal number, we can simply add the first n positive integers each multiplied by 7i−1 where i is the index.
"""


"""
We can check if a number is a nonagonal number by checking if it is divisible by 7, since all nonagonal numbers are divisible by 7.
"""


"""
To