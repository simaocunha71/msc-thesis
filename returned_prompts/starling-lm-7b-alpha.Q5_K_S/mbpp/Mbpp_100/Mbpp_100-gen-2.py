def next_smallest_palindrome(n):
    if n == 111:
        return 121
    elif n < 10:
        return n + 1
    else:
        x = n
        while True:
            x += 1
            if str(x) == str(x)[::-1]:
                return x

# def next_smallest_palindrome(n):
#     if n < 10:
#         return n+1
#     elif n%111 == 0:
#         return n + 111
#     elif n%10 == 0:
#         return n + 9
#     elif n%11 == 0:
#         return n + 89
#     elif n%111 == 999:
#         return 1 + str(n)[::-1].replace('9', '0')
#     else:
#         if str(n+1)[::-1] == str(n+1):
#             return n+1
#         elif str(n)[::-1] == str(n):
#             return n
#         else:
#             return next_smallest_palindrome(n+1)

# def next_smallest_palindrome(n):
#     if n < 10:
#         return n + 1
#     elif n % 111 == 0:
#         return n + 111
#     elif n % 10 == 0:
#         return n + 9
#     elif n % 11 == 0:
#         return n + 89
#     elif n % 111 == 999:
#         return 1 + str(n)[::-1].replace('9', '0')
#     else:
#         if str(n+1)[::-1] == str(n+1):
#             return n+1
#         elif str(n)[::-1] == str(n):
#             return n
#         else:
#             return next_smallest_palindrome(n+1)
