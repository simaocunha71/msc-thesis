
def skjkasdkd(lst):
    largest_prime = 0
    for num in lst:
        if num > largest_prime and is_prime(num):
            largest_prime = num
    return sum(str(largest_prime))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))
print(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]))
print(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]))
print(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]))
print(skjkasdkd([0,81,12,3,1,21]))
print(skjkasdkd([0,8,1,2,1,7]))
print(skjkasdkd([0,78,2,7,78,2,7]))
print(skjkasdkd([0,8,1,2,1,7,0,8,1,2,1,7]))
print(skjkasdkd([0,78,2,7,78,2,7,0,8,1,2,1,7]))
print(skjkasdkd([0,78,2,7,78,2,7,0,8,1,2,1,7,