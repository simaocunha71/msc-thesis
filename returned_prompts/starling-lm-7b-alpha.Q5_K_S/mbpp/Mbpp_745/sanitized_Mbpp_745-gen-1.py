from itertools import chain
from operator import mul
def divisible_by_digits(startnum, endnum):
    def digits(num):
        return (int(d) for d in str(num))
    return list(chain(*[set(xrange(startnum, endnum + 1)) for x in [reduce(mul, digits(n)) for n in xrange(startnum, endnum + 1)]]))