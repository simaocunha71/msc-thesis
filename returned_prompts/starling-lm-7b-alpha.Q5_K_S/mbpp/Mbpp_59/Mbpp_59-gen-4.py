def is_octagonal(n):
    if n==1:
        return True
    elif n%2==1:
        return is_octagonal(n-1) and is_octagonal(n-3)
    elif n%8==0:
        return is_octagonal(n/8)
    else:
        return False

def octagonal(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    elif n%2==1:
        return octagonal(n-1)+octagonal(n-3)
    elif n%8==0:
        return octagonal(n/8)
    else:
        return octagonal(n-1)+octagonal(n-3)+octagonal(n-7)+octagonal(n-5)

# assert is_octagonal(5) == True
# assert is_octagonal(6) == True
# assert is_octagonal(7) == False
# assert is_octagonal(8) == True
# assert is_octagonal(9) == True
# assert is_octagonal(10) == True
# assert is_octagonal(11) == False
# assert is_octagonal(12) == True
# assert is_octagonal(13) == True
# assert is_octagonal(14) == True
# assert is_octagonal(15) == True
# assert is_octagonal(16) == True
# assert is_octagonal(17) == True
# assert is_octagonal(18) == True
# assert is_octagonal(19) == True
# assert is_octagonal(20) == True
# assert is_octagonal(21) == True
# assert is_octagonal(22) == True
# assert is_octagonal(23) == True
# assert is_octagonal(24) == True
# assert is_octagonal(25) == True
# assert is_octagonal(26) == True
# assert is_octagonal(27) == True
# assert is_octagonal(28) == True
# assert is_octagonal(29) == True