```
def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if n == 2:
        return m * (m - 1) // 2
    if n == 3:
        return m * (m - 1) * (m - 2) // 6
    total = 0
    for i in range(2, m):
        total += get_total_number_of_sequences(i, n - 1)
    return total
```


The problem asks to find the number of possible sequences of length n, where each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.

The base case for this problem is when n is 1, in which case the total number of sequences is equal to m, since there are m possible values for the first element.

When n is 2, the total number of sequences is equal to m * (m - 1) // 2, since the second element is less than or equal to m and greater than or equal to twice the first element.

When n is 3, the total number of sequences is equal to m * (m - 1) * (m - 2) // 6, since the third element is less than or equal to m and greater than or equal to twice the second element.

For n greater than 3, the total number of sequences is found by summing up the total number of sequences for each possible value of the first element. This is because each possible value of the first element corresponds to a unique sequence of length n.

The function get_total_number_of_sequences(m, n) implements this logic using recursion. It takes in two positive integers m and n as input and returns the total number of possible sequences of length n. The base cases for n being 1, 2, or 3 are handled separately, and for n greater than 3, the function recursively calls itself with the updated value of m and n - 1. The total number of sequences is then returned as the sum of the total number of sequences for each possible value of the first element.

The unit test `assert get_total_number_of_sequences(10, 4) == 4` helps to verify the correctness of the function. It checks that the total number of possible sequences of length 4 with elements less than or equal to 10 is indeed 4. This test can be used to