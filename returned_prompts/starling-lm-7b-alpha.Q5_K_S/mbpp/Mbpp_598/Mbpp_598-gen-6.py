"""
def armstrong_number(n):
    summ=0
    temp=n
    while temp>0:
        digit=temp%10
        summ+=digit**3
        temp//=10
    if summ==n:
        return True
    else:
        return False
"""

def armstrong_number(n):
    n = str(n)
    length = len(n)
    total = 0
    for i in n:
        total += int(i) ** length
    return total == int(n)

assert armstrong_number(153)==True
print(armstrong_number(153))
print(armstrong_number(370))
print(armstrong_number(371))
print(armstrong_number(9))
print(armstrong_number(10))

#print(armstrong_number(153))
#print(armstrong_number(370))
#print(armstrong_number(371))
#print(armstrong_number(9))
#print(armstrong_number(10))


"""
"""

def armstrong_number(n):
    summ = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        summ += digit ** len(str(n))
        temp //= 10
    if summ == n:
        return True
    else:
        return False

assert armstrong_number(153) == True
print(armstrong_number(153))
print(armstrong_number(370))
print(armstrong_number(371))
print(armstrong_number(9))
print(armstrong_number(10))

"""
"""

def armstrong_number(n):
    summ = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        summ += digit ** len(str(n))
        temp //= 10
    if summ == n:
        return True
    else:
        return False

assert arm