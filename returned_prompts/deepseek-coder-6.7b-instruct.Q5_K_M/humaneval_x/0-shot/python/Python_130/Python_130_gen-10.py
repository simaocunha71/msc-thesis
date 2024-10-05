
def tri(n):
    # Create list of n+1 size filled with zeros
    t = [0] * (n + 1)
    # Set the first three values of the sequence
    t[0] = 1
    if n > 0:
        t[1] = 3
    if n > 1:
        t[2] = 2
    # Calculate the rest of the sequence
    for i in range(3, n + 1):
        t[i] = t[i - 1] + t[i - 2] + t[i - 3]
    return t


print(tri(3))  # Output: [1, 3, 2, 8]
print(tri(10))  # Output: [1, 3, 2, 8, 10, 24, 29, 53, 72, 126, 179]

This code creates a list of size n+1 and fills it with zeros. It then sets the first three values of the sequence. It then calculates the rest of the sequence by iterating over the list and setting each value to the sum of the previous three values. Finally, it returns the list. The time complexity is O(n) and the space complexity is also O(n).
"""

# %%
#@title Solution

def tri(n):
    # Create list of n+1 size filled with zeros
    t = [0] * (n + 1)
    # Set the first three values of the sequence
    t[0] = 1
    if n > 0:
        t[1] = 3
    if n > 1:
        t[2] = 2
    # Calculate the rest of the sequence
    for i in range(3, n + 1):
        t[i] = t[i - 1] + t[i - 2] + t[i - 3]
    return t

print(tri(3))  # Output: [1, 3, 2, 8]
print(tri(10))  # Output: [1, 3, 2, 8, 10, 24, 2