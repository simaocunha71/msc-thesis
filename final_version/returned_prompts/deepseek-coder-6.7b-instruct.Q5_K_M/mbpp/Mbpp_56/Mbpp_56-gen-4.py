def check(n):
    s = str(n)
    rev = s[::-1]
    return n == int(rev)*2 - 1

print(check(70))

#Output: False

#Explanation: Reverse of 70 is 07 which when multiplied by 2 gives 14 but 70 is not 1 less than 14. Hence the output is False.

#Test Cases:
assert check(11) == True
assert check(121) == True
assert check(12321) == True
assert check(12344) == False
assert check(100) == True
assert check(70) == False
assert check(1234321) == False
assert check(10) == True
assert check(1) == False
assert check(1000) == False
assert check(123454321) == True
assert check(12345654321) == False
assert check(1234567654321) == False
assert check(123456787654321) == True
assert check(123456789987654321) == True
assert check(1234567890987654321) == False
assert check(12345678910987654321) == False
assert check(123456789111987654321) == True
assert check(1234567891111987654321) == False
assert check(12345678911111987654321) == False
assert check(123456789111111987654321) == True
assert check(1234567891111111987654321