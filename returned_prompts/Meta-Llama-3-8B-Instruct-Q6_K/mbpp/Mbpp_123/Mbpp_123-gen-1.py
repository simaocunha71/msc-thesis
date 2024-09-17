```
def amicable_numbers_sum(n):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)

    total = 0
    for i in range(2, n):
        a = sum_of_divisors(i)
        b = sum_of_divisors(a)
        if i == b and i != a:
            total += i + a
    return total
```


```
def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)

def amicable_numbers_sum(n):
    total = 0
    for i in range(2, n):
        a = sum_of_divisors(i)
        b = sum_of_divisors(a)
        if i == b and i != a:
            total += i + a
    return total
```


```
def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)

def amicable_numbers_sum(n):
    total = 0
    for i in range(2, n):
        a = sum_of_divisors(i)
        b = sum_of_divisors(a)
        if i == b and i != a:
            total += i + a
    return total
```


```
def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)

def amicable_numbers_sum(n):
    total = 0
    for i in range(2, n):
        a = sum_of_divisors(i)
        b = sum_of_divisors(a)
        if i == b and i != a:
            total += i + a
    return total
```


```
def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)

def amicable_numbers_sum(n):
    total = 0
    for i in range(2, n):
        a = sum_of_divisors(i)
        b = sum_of_divisors(a)
        if i == b and i != a:
            total += i + a
    return total
```


```
def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)

def amicable_numbers_sum(n):
    total = 