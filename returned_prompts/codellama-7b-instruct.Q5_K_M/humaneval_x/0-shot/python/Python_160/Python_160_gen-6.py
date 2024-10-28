
from functools import reduce

def do_algebra(operator, operand):
    return reduce(lambda x, y: x(y), map(operator.index, operand), operator[0])(operand[-1])
