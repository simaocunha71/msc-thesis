"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
import math

def prime_num(n):
    is_prime = True
    while is_prime:  # 在while子句中的is_prime变量是有效的，因为是作用于while语句内部的
        if n==1 or n==0 : # 若是一或者零则返回True
            is_prime = False # 将n指向一或者零，则返回False
    else:   # 若仍然不能判断为一或者零的话
        i=2; j=int(math.sqrt(n)); while i<j: # 找到n/i时间的最小值
            if (n % i) ==0 : is_prime = False # 若是一或者乘以几何根数，则返回False
        else:    i=int(math.sqrt(n))+1; j=3*(j-i); while i<j: 
            if (n % i) ==0 : is_prime = False # 若仍然不能用几何根数，则使用庭院根数来判断是一或者乘以庭院根数时间的最小值
        else:    n=int(n/i); i+=2; j=3*(j-i) # 如果至此不能判断，则使用其他方法来判断是一或者乘以庭院根数时间的最小值
    return is_prime
print(prime_num(1)) #输出True
