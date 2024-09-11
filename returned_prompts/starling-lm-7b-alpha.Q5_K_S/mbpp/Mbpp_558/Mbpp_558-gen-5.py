def digit_distance_nums(n, m):
    nd = str(n)
    md = str(m)
    if len(nd) != len(md):
        return False
    else:
        ndigits = len(nd)
        res = 0
        for i in range(ndigits):
            res += abs(int(nd[i]) - int(md[i]))
    return res

#Test
assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(123, 456) == 31
assert digit_distance_nums(1234, 5678) == 18

# Test with negative numbers
assert digit_distance_nums(9876, -1234) == 21
assert digit_distance_nums(-1234, 9876) == 21

# Test with single digit numbers
assert digit_distance_nums(5, 6) == 1
assert digit_distance_nums(-5, 6) == 1
assert digit_distance_nums(5, -6) == 1

# Test with zero
assert digit_distance_nums(0, 0) == 0
assert digit_distance_nums(0, -0) == 0
assert digit_distance_nums(-0, 0) == 0

# Test with a single digit and a multi-digit number
assert digit_distance_nums(5, 67) == 12
assert digit_distance_nums(-5, 67) == 12
assert digit_distance_nums(5, -67) == 12

# Test with a multi-digit and a single-digit number
assert digit_distance_nums(67, 5) == 12
assert digit_distance_nums(-67, 5) == 12
assert digit_distance_nums(67, -5) == 12

# Test with zero and a multi-digit number
assert digit_distance_nums(0, 67) == 6