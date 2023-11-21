
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    s = set()
    for i in range(9): # this is the maximum value of n and hence the length of number we want to generate
        str_num = ''.join([str(i) for i in range(n)]) + str(10**(len(s)+1))[-1]
        if s.count(str_num) == 1: return (1, len(s), len(str(s.count('1'))))
        s.add(str_num)
    return None, None, None

if __name__ == '__main__':
    print(starts_one_ends(-99999999))