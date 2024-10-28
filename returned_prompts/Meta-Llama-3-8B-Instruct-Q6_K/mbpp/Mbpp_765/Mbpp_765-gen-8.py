def is_polite(n):
    def is_polite_number(m):
        sum1 = 0
        sum2 = 0
        for i in range(1, m):
            if m % i == 0:
                sum1 += i
            if i % m == 0:
                sum2 += i
        if sum1 == m and sum2 == m:
            return True
        return False

    count = 0
    i = 1
    while True:
        if is_polite_number(i):
            count += 1
            if count == n:
                return i
        i += 1

def nth_polite_number(n):
    return is_polite(n)
assert nth_polite_number(7) == 11
assert nth_polite_number(4) == 6
assert nth_polite_number(5) == 8
assert nth_polite_number(1) == 2
assert nth_polite_number(2) == 4
assert nth_polite_number(3) == 6
assert nth_polite_number(6) == 28
assert nth_polite_number(8) == 48
assert nth_polite_number(9) == 56
assert nth_polite_number(10) == 88
assert nth_polite_number(11) == 104
assert nth_polite_number(12) == 124
assert nth_polite_number(13) == 180
assert nth_polite_number(14) == 220
assert nth_polite_number(15) == 240
assert nth_polite_number(16) == 264
assert nth_polite_number(17) == 280
assert nth_polite_number(18) == 320
assert nth_polite_number(19) == 336
assert nth_polite_number(20) == 352
assert nth_polite_number(21) == 360
assert nth_polite_number(22) == 384
assert nth_polite_number(23) == 408
assert nth_polite_number(24) == 432
assert nth_polite_number(25) == 456
assert nth_polite_number(26) == 480
assert nth_polite_number(27) == 504
assert nth_polite_number(28) == 528
assert nth_polite_number(29) == 552
assert nth_polite_number(30) == 576
assert nth_polite