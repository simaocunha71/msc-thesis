
def count_up_to(n):
    prime_array = []
    for i in range(2,n):
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_array.append(i)
    return prime_array

# def count_up_to(n):
#     prime_array = []
#     for i in range(2,n):
#         if all(i % j != 0 for j in range(2,i)):
#             prime_array.append(i)
#     return prime_array



print(count_up_to(10))  # []
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(100))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(count_up_to(101))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(count_up_to(0))  # []
print(count_up_to(1))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(18))  #