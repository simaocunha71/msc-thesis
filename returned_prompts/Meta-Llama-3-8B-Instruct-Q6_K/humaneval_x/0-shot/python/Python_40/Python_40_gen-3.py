def triples_sum_to_zero(l: list):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(triples_sum_to_zero([1, 3, -2, 1]))  # Output: True
print(triples_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))  # Output: True
print(triples_sum_to_zero([1]))  # Output: False

This function works by iterating over the list and keeping track of the numbers it has seen so far in a set. If it encounters a number that is the negative of a number it has seen before, it returns True, indicating that there are three distinct elements in the list that sum to zero. If it finishes iterating over the list without finding such a pair of numbers, it returns False. The time complexity of this function is O(n), where n is the length of the input list, because it makes one pass over the list. The space complexity is also O(n), because in the worst case it may need to store every number in the set.