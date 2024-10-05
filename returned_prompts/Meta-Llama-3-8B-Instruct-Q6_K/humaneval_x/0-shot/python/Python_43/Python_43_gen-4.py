def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x * -1 in seen:
            return True
        seen.add(x)
    return False
# This function goes through the list, adding each element to a set.
# If it finds an element that is the negative of an element that has been seen before, it immediately returns True.
# If it goes through the whole list without finding such a pair, it returns False.