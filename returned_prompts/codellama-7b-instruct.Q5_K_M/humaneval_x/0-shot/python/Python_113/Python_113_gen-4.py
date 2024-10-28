
def odd_count(lst):
    return ['the number of odd elements %d in the string %d of the input.' % (odd_count_helper(s), i) for i, s in enumerate(lst)]

def odd_count_helper(s):
    return sum(1 for c in s if c != '0' and int(c) % 2)
