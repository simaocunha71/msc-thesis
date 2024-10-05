
def count_up_to(n):
    primes = []
    for i in range(2,n):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

# def count_up_to(n):
#     primes = []
#     for i in range(2,n+1):
#         if check_prime(i):
#             primes.append(i)
#     return primes

# def check_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# def check_prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# def check_prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# def check_prime(n):
#     return len([i for i in range(2,int(n**0.5)+1) if n%i == 0]) == 0

# def check_prime(n):
#     return len([i for i in range(2,int(n**0.5)+1) if n%i == 0]) == 0

# def check_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# def check_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# def check_prime(n):
#     for i in range(