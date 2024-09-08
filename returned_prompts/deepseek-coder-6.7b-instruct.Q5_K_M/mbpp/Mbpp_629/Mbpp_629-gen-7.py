def find_multiples_of_two_and_three(lst):
    return [num for num in lst if num % 2 == 0 and num % 3 == 0]

print(find_multiples