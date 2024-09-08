def count_num(lst):
    even_count = sum(1 for num in lst if num % 2 == 0)
    odd_