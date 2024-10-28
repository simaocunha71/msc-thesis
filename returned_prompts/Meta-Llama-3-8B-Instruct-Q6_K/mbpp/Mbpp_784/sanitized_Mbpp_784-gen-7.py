def mul_even_odd(lst):
    even_num = next((num for num in lst if num % 2 == 0), None)
    odd_num = next((num for num in lst if num % 2 != 0), None)
    return even_num * odd_num if even_num and odd_num else 0