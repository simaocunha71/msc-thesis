    seen = set()
    for num in l:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False
    # This function works by iterating over the list, for each number, it calculates its complement
    # (the number that would be needed to make the sum equal to zero), it then checks if this complement
    # is in the set of seen numbers, if it is, it means that we have found three numbers that sum to zero
    # and it returns True. If no such numbers are found, it returns False.


