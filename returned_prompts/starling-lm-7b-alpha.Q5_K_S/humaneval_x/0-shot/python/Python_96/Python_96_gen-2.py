
def count_up_to(n):
    if n == 0:
        return []
    if n == 1:
        return []
    result = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result

# def count_up_to(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return []
#     result = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             result.append(i)
#     return result

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def count_up_to(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return []
#     result = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             result.append(i)
#     return result

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def count_up_to(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return []
#     result = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             result.append(i)
#     return result

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range