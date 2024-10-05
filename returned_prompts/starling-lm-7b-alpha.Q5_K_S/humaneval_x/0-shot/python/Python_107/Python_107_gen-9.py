
def even_odd_palindrome(n):
    even_list = []
    odd_list = []
    for i in range(1, n+1):
        str_i = str(i)
        if str_i == str_i[::-1]:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
    return (len(even_list), len(odd_list))


# Time:  O(n)
# Space: O(1)
def even_odd_palindrome_optimized(n):
    even_list = []
    odd_list = []
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
    return (len(even_list), len(odd_list))

```