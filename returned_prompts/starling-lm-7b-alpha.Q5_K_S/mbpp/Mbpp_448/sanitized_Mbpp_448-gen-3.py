def cal_sum(n):
    # Step 1: Create an empty list to store the Perrin numbers.
    perrin_numbers = []

    # Step 2: Iterate through all the numbers less than n.
    for i in range(1, n):
        # Step 3: Check if a number can be expressed as the sum of two positive integers in exactly one way. If it can, add it to the list of Perrin numbers.
        if all(i % j != 0 for j in range(1, i)):
            perrin_numbers.append(i)

    # Step 4: Calculate the sum of the Perrin numbers in the list.
    sum_perrin_numbers = sum(perrin_numbers)

    # Step 5: Return the sum.
    return sum_perrin_numbers