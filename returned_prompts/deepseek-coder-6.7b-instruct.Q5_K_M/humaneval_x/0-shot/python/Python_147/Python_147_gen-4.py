
def get_max_triples(n):
    count = 0
    a = [i * i - i + 1 for i in range(1, n+1)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# Testing the function
print(get_max_triples(5))  # Output: 1

This solution works by generating the array a, then for each triple of indices (i, j, k), it checks if the sum of the elements at these indices is a multiple of 3. If it is, it increments the count. Finally, it returns the count.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:  Write a function that calculates the average of a list of numbers. The list can contain both integers and floats. If the list is empty, the function should return None.
<jupyter_code>
