
def f(n):
    # Create a list of size n
    result = [None] * n

    # Initialize the first element
    result[0] = 1

    # Fill the rest of the list
    for i in range(1, n):
        # If the index is even
        if i % 2 == 0:
            result[i] = i * result[i - 1]
        # If the index is odd
        else:
            result[i] = sum(range(1, i + 1))

    return result

# Test the function
print(f(5))

