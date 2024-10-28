    return [f"the number of odd elements {odd_digits}n the str{odd_digits}ng {i} of the {odd_digits}nput." for i, odd_digits in enumerate(sum(map(lambda s: sum(map(int, filter(lambda c: int(c) % 2 != 0, s))), lst)))]

I'm assuming that the "odd elements" refers to the digits in the string which are odd (i.e., 1, 3, 5, 7, 9).

