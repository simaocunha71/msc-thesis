def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            result.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return result


# Python3 program to print all combinations of sums of tuples
# from the given tuple list
def print_sum_combinations(tuples):

    # Stores all the combinations of sums of tuples
    result = []

    # Iterate through each tuple in the given list
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):

            # Find the sum of the first and second tuple
            sum_comb = (tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1])

            # Append the sum_comb to the result
            result.append(sum_comb)

    # Return the result
    return result


# Driver code
print(print_sum_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))

# This code is contributed by PrinciRaj11


def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            result.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return result


# Python3 program to print all combinations of sums of tuples
# from the given tuple list
def print_sum_combinations(tuples):

    # Stores all the combinations of sums of tuples
    result = []

    # Iterate through each tuple in the given list
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):

           