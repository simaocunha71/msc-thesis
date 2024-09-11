def find(x,y):
    return x//y

# Python program to check if a number is prime or not


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    # This is checked so that we can skip middle five numbers in the below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

# Driver program
#n = int(input("Enter a number:"))
#if (isPrime(n)):
#    print("Prime")
#else:
#    print("Not Prime")

# Python program to print the first n
# natural numbers that are prime

def print_prime(n):
    prime = []
    k = 2
    while len(prime) < n:
        if isPrime(k):
            prime.append(k)
        k += 1
    return prime

# Driver program
#n = int(input("Enter a number:"))
#prime_list = print_prime(n)
#print(prime_list)

# Python program to print the sum of first n natural
# numbers that are prime

def prime_sum(n):
    prime_list = print_prime(n)
    sum = 0
    for i in range(len(prime_list)):
        sum += prime_list[i]
    return sum

# Driver program
#n = int(input("Enter a number:"))
#sum_prime_num = prime_sum(n)
#print(sum_prime_num)

# Python Program to print the product of first n
# natural numbers that are prime

def prime_product(n):
    prime_list = print_prime(n)
    product = 1
    for i in range(len(prime_list)):
        product *= prime_list[i]
    return product