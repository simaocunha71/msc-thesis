def digits(n):
    odd = [x for x in str(n) if int(x) % 2 != 0]
    if len(odd) == 0:
        return 0
    else:
        return eval('*'.join(odd))

print(digits(1))  == 1
print(digits(4))  == 0
print(digits(235)) == 15
print(digits(12345)) == 15
print(digits(0))  == 0
print(digits(2))  == 0
print(digits(3))  == 3
print(digits(4))  == 0
print(digits(5))  == 5
print(digits(6))  == 0
print(digits(7))  == 7
print(digits(8))  == 0
print(digits(9))  == 9
print(digits(123456789)) == 945
print(digits(1111111111)) == 0
print(digits(666666666)) == 0
print(digits(444444444)) == 0
print(digits(888888888)) == 0
print(digits(999999999)) == 0