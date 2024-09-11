"""
def get_pairs_count(numbers, sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                count += 1
    return count

print(get_pairs_count([1,1,1,1], 2))
"""

def get_pairs_count(numbers, sum):
    return sum(map(lambda x: len([1 for y in numbers if y == sum-x]), numbers))

print(get_pairs_count([1,1,1,1], 2))

