"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""

def find_even_pair(numbers):
    """Counts how many pairs evenly sum to an even number."""  
    if not isinstance(numbers, list):
        numbers = [numbers]
    
    even_count = 0
    for num in numbers:
        if (not (num % 2 == 0) and int(even_count + num / 2) % 2 == 0):
            print('Number not evenly divisible by two')
            pass
        else:
            print('Number evenly divisible by two')
            even_count += num/2
    return even_count
