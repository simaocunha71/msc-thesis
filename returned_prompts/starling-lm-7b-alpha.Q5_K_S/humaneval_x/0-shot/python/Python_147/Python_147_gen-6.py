
# First, we define the function get_max_triples that takes a positive integer n as input.
# We initialize a variable result to 0, which will keep track of the number of valid triples.

# Then, we define a function called generate_array that takes the length of the array as input and returns the array itself.
# Inside this function, we use list comprehension to create the array a of length n. Each element of the array is calculated as i * i - i + 1, where i ranges from 1 to n.

# Next, we use nested loops to iterate over all possible combinations of i, j, and k indices in the array.
# We check if i < j < k condition is satisfied, and if the sum of the corresponding elements a[i], a[j], and a[k] is divisible by 3.
# If these conditions are satisfied, we increment the result variable by 1.

# Finally, we return the value of the result variable, which gives us the number of valid triples.

def get_max_triples(n):
    result = 0

    def generate_array(length):
        return [i * i - i + 1 for i in range(1, length + 1)]

    a = generate_array(n)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    result += 1

    return result

# Example usage:
n = 5
print(get_max_triples(n))  # Output: 1

# In this example, the input n is 5, which means we have an array a of length 5. The function generates the array [1, 3, 7, 13, 21].
# We then iterate over all possible combinations of indices i, j, and k, and check if the sum of the corresponding elements is divisible by 3.
# In this case, the only valid triple is (1, 7, 13), so the function returns 1 as the result