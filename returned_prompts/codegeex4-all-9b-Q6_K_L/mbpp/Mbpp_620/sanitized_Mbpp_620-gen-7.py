def largest_subset(numbers):
    def is_divisible(a, b):
        return a % b == 0 or b % a == 0

    def recurse(numbers, current_subset, largest_subset):
        if not numbers:
            return max(largest_subset, current_subset)

        head, *tail = numbers
        new_subset = current_subset + [head] if is_divisible(current_subset[-1], head) else current_subset
        largest_subset = recurse(tail, new_subset, largest_subset)
        largest_subset = recurse(tail, current_subset, largest_subset)

        return largest_subset

    return recurse(numbers, [numbers[0]], [numbers[0]])