"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""

def get_pairs_count(numbers, sum):
    pairs = []

    for pair in zip(numbers, numbers[1:]):
        if sum in pair and pair[0]+pair[-1] == sum:
            pairs.append(pair)
    return len(pairs)

print(get_pairs_count([1, 2, 3], 6))
