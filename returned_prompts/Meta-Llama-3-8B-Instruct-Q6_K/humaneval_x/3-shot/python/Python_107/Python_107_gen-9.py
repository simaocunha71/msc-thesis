    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n + 1):
        str_num = str(i)
        if str_num == str_num[::-1]:
            if int(str_num) % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes


