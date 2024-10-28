

def largest_divisor(n: int) -> int:
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1

print(largest_divisor(15))

#Alternate solution using a loop and a built-in function

def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

print(largest_divisor(15))

#Alternate solution using list comprehension

def largest_divisor(n: int) -> int:
    return max([i for i in range(1, n) if n % i == 0])

print(largest_divisor(15))


#Alternate solution using a loop and a built-in function

def largest_divisor(n: int) -> int:
    for i in reversed(range(1, n)):
        if n % i == 0:
            return i

print(largest_divisor(15))


#Alternate solution using a while loop

def largest_divisor(n: int) -> int:
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1

print(largest_divisor(15))

#Alternate solution using a loop and a built-in function

def largest_divisor(n: int) -> int:
    for i in reversed(range(1, n)):
        if n % i == 0:
            return i

print(largest_divisor(15))


#Alternate solution using list comprehension

def largest_divisor(n: int) -> int:
    return max([i for i in range(1, n) if n % i == 0])

print(largest_divisor(15))

#Alternate solution using a while loop

def largest_divisor(n: int) -> int:
    i = n - 