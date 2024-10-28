
    # Function to check divisibility by 3
    def is_divisible_by_three(n: int) -> bool:
        return n % 3 == 0

    # Getting the values at the indices divisible by 3
    divisible_by_three_values = [l[i] for i in range(len(l)) if is_divisible_by_three(i)]

    # Sorting the values
    divisible_by_three_values.sort()

    # Replacing the values at the indices divisible by 3 in the original list
    for i in range(len(l)):
        if is_divisible_by_three(i):
            l[i] = divisible_by_three_values.pop(0)

    return l


print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2