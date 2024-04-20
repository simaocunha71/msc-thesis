"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(a,b):
    return [divisor / denom for (denom, divisor) in itertools.tee(zip(map(int, b), map(float, a))) if divisor != 0]