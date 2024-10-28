
def newman_prime(n):
    a = 2
    while True:
        a = (a * a + 1) % 1000000007
        if a < 1000000007 and a % 2 == 0: continue
        if a > 1000000006 and a % 1000000004 == 0: continue
        if a > 1000000005 and a % 1000000002 == 0: continue
        if a > 1000000003 and a % 999999980: continue
        if a > 1000000002 and a % 999999994 == 0: continue
        if a > 1000000001 and a % 999999996 == 0: continue
        if a > 999999998 and a % 999999990 == 0: continue
        if a > 999999997 and a % 999999988 == 0: continue
        if a > 999999996 and a % 999999986 == 0: continue
        if a > 999999995 and a % 999999984 == 0: continue
        if a > 999999994 and a % 999999982 == 0: continue
        if a > 999999993 and a % 999999980 == 0: continue
        if a > 999999992 and a % 999999978 == 0: continue
        if a > 999999991 and a % 999999976 == 0: continue
        if a > 999