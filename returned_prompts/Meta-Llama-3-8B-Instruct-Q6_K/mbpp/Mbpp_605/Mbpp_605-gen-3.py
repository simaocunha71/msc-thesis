```
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```    
    This function takes an integer `n` as input and returns `True` if it is a prime number, and `False` otherwise. It first checks if `n` is less than or equal to 1, in which case it is not prime. Then it iterates from 2 to the square root of `n` (inclusive), and for each `i` in this range, it checks if `n` is divisible by `i`. If it is, then `n` is not prime and the function returns `False`. If `n` is not divisible by any `i` in this range, then it is prime and the function returns `True`. The unit test `assert prime_num(13)==True` ensures that the function correctly identifies prime numbers.    
    



```
python
```
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```
    This function takes an integer `n` as input and returns `True` if it is a prime number, and `False` otherwise. It first checks if `n` is less than or equal to 1, in which case it is not prime. Then it iterates from 2 to the square root of `n` (inclusive), and for each `i` in this range, it checks if `n` is divisible by `i`. If it is, then `n` is not prime and the function returns `False`. If `n` is not divisible by any `i` in this range, then it is prime and the function returns `True`. The unit test `assert prime_num(13)==True` ensures that the function correctly identifies prime numbers.    
    



```
python
```
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
```
    This function takes an integer `n