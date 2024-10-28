
    even = 0
    odd = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

# --------------------------------------

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    num = abs(num)
    even = sum(1 for digit in str(num) if int(digit) % 2 == 0)
    odd = sum(1 for digit in str(num) if int(digit) % 2 == 1)
    return (even, odd)

# --------------------------------------

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> タプル(1, 1)
        even_odd_count(123) を返します(1, 2)
    """

    num = abs(num)
    even = sum(int(i) % 2 == 0 for i in str(num))
    odd = sum(int(i) % 2 == 1 for i in str(num))
    return (even, odd)

# --------------------------------------

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ➞ (1, 1)
        even_odd_count(123) ➞ (1, 2)
    """

    even = sum(1 for i in str(abs(num)) if int(i) % 2 == 0)
    odd = sum(1 for i in str(abs(num)) if