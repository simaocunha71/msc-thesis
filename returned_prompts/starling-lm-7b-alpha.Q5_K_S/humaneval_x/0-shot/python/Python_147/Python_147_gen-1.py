
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# Test case
n = 5
print(get_max_triples(n))

# Output: 1
# Explanation:
# a = [1, 3, 7, 13, 21]
# The only valid triple is (1, 7, 13).


def get_max_triples(n):
    # Create an array of length n
    a = [i * i - i + 1 for i in range(1, n + 1)]

    # Initialize a counter to keep track of the number of valid triples
    count = 0

    # Iterate over all possible combinations of i, j, and k
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the sum of a[i], a[j], and a[k] is divisible by 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # If it is, increment the counter
                    count += 1

    # Return the total number of valid triples
    return count

# Test case
n = 5
print(get_max_triples(n))  # Output: 1

# Explanation:
# The array a is created as follows: [1, 3, 7, 13, 21].
# The only valid triple in this array is (1, 7, 13), which satisfies the condition (a[i] + a[j] + a[k]) % 3 == 0.
# Therefore