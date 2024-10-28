
def count_up_to(n):
    if n == 0:
        return []
    if n == 1:
        return [2]
    prime_nums = [2,3]
    for i in range(5, n + 1, 2):
        is_prime = True
        for p in prime_nums:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(i)
    return prime_nums[:n]


# count_up_to(5) => [2,3]
# count_up_to(11) => [2,3,5,7]
# count_up_to(0) => []
# count_up_to(20) => [2,3,5,7,11,13,17,19]
# count_up_to(1) => []
# count_up_to(18) => [2,3,5,7,11,13,17]


# count_up_to(99) => [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]





# def count_up_to(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return [2]
#     prime_nums = [2,3]
#     for i in range(5, n + 1, 2):
#         is_prime = True
#         for p in prime_nums:
#             if i % p == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_nums.append(i)
#     return prime