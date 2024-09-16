def next_smallest_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    str_n = str(n)
    if str_n == str_n[::-1]:
        return int(str_n) + 1
    else:
        for i in range(len(str_n)):
            if str_n[i] != str_n[-i-1]:
                break
        return int(str_n[:i] + str(int(str_n[i]) + 1) + str_n[i+1:])