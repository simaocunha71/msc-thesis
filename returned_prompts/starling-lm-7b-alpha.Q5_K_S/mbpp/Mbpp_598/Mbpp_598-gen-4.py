def armstrong_number(n):
    num=n
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem**3)
        num=num//10
    if(sum==n):
        return True
    else:
        return False

"""
def armstrong_number(n):
    num=n
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem**3)
        num=num//10
    if(sum==n):
        return True
    else:
        return False
"""
"""
def armstrong_number(n):
    num = n
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** 3
        num //= 10
    if sum == n:
        return True
    else:
        return False
"""
"""
def armstrong_number(n):
    sum=0
    while(n>0):
        rem=n%10
        sum=sum+(rem**3)
        n=n//10
    if(sum==n):
        return True
    else:
        return False
"""

def armstrong_number(n):
    if(n<0):
        return False
    else:
        digits = len(str(n))
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** digits
            n //= 10
        if sum == n:
            return True
        else:
            return False


"""
def armstrong_number(n):
    digits = len(str(n))
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** digits
        n //= 10
    if sum == n:
        return True
    else:
        return False
"""

"""
def armstrong_number(n):
    digits = len(str(n))
    sum = 0
    while n > 