
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    def get_digits(num):
        return [i for i in num]

    digits = get_digits(num)
    evens = int(len([x for x in digits if x % 2 == 0]))
    odds = int(len([x for x in digits if x % 2 != 0]))
    return (evens, odds)
