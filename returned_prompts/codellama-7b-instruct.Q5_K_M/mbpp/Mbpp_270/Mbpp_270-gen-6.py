
def sum_even_and_even_index(my_list: list) -> int:
    total = 0
    for i, x in enumerate(my_list):
        if i % 2 == 0 and x % 2 == 0:
            total += x
    return total


