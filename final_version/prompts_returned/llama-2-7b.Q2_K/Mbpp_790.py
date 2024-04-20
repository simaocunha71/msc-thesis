"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""

def even_position(numbers):
    for i in range(len(numbers)):  # 0-indexed
        if not (i % 2 != 0) and numbers[i] % 2 == 0:
            return True
    return False
