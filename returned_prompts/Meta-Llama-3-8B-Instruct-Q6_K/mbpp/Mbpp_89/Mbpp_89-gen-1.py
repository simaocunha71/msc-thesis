def closest_num(n):
    for i in range(n-1, -1, -1):
        if i < n:
            return i
    return None

# Test the function
print(closest_num(11))  # Output: 10
print(closest_num(100))  # Output: 99
print(closest_num(1))  # Output: None
print(closest_num(2))  # Output: 1
print(closest_num(0))  # Output: None
print(closest_num(5))  # Output: 4
print(closest_num(8))  # Output: 7
print(closest_num(9))  # Output: 8
print(closest_num(10))  # Output: 9
print(closest_num(11))  # Output: 10
print(closest_num(12))  # Output: 11
print(closest_num(15))  # Output: 14
print(closest_num(20))  # Output: 19
print(closest_num(21))  # Output: 20
print(closest_num(22))  # Output: 21
print(closest_num(25))  # Output: 24
print(closest_num(30))  # Output: 29
print(closest_num(31))  # Output: 30
print(closest_num(32))  # Output: 31
print(closest_num(35))  # Output: 34
print(closest_num(40))  # Output: 39
print(closest_num(41))  # Output: 40
print(closest_num(42))  # Output: 41
print(closest_num(45))  # Output: 44
print(closest_num(50))  # Output: 49
print(closest_num(51))  # Output: 50
print(closest_num(52))  # Output: 51
print(closest_num(55))  # Output: 54
print(closest_num(60))  # Output: 59
print(closest_num(61))  # Output: 60
print(closest_num(62))  # Output: 61
print(closest_num(65))  # Output: 64
print(closest_num(70))  # Output: 69
print(closest_num(71))  # Output: 70