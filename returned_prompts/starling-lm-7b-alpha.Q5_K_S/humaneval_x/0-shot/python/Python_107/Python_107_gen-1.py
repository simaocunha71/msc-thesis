
def even_odd_palindrome(n):
    count_odd = 0
    count_even = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            if str(i) == str(i)[::-1]:
                count_even += 1
        else:
            if str(i) == str(i)[::-1]:
                count_odd += 1
    return (count_even, count_odd)


# Test cases
print(even_odd_palindrome(3))  # (1, 2)
print(even_odd_palindrome(12))  # (4, 6)






```
