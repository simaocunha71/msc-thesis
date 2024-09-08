def square_Num(num):
    if isinstance(num, int) and num >= 0:
        return num ** 2
    else:
        return 'Invalid'

print(square_Num(5)) # should return 25
print(square_Num(0)) # should return 0
print(square_Num(-5)) # should return 'Invalid'
print(square_Num('a')) # should return 'Invalid'


"""
Write a python function to check if a given number is prime or not.
assert check_Prime(5) == True
assert check_Prime(4)