def dif_Square(n):
    i = 0
    while i * i <= n:
        j = 0
        while j * j <= n:
            if i * i + j * j == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5))  # True

# Test case 2
assert dif_Square(5) == True

# Test case 3
assert dif_Square(3) == True

# Test case 4
assert dif_Square(2) == False

# Test case 5
assert dif_Square(1) == True

# Test case 6
assert dif_Square(0) == True

# Test case 7
assert dif_Square(4) == True

# Test case 8
assert dif_Square(6) == False

# Test case 9
assert dif_Square(7) == False

# Test case 10
assert dif_Square(8) == False

# Test case 11
assert dif_Square(9) == True

# Test case 12
assert dif_Square(10) == False

# Test case 13
assert dif_Square(11) == False

# Test case 14
assert dif_Square(12) == False

# Test case 15
assert dif_Square(13) == False

# Test case 16
assert dif_Square(14) == False

# Test case 17
assert dif_Square(15) == False

# Test case 18
assert dif_Square(16) == True

# Test case 19
assert dif_Square(17) == False

# Test case 20
assert dif_Square(18) == False

# Test case 21
assert dif_Square(19) == False

# Test case 22
assert dif_Square(20) == False

# Test case 23
assert dif_Square(21) == False

# Test case 24