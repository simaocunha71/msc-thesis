# Here's a step-by-step guide to solve this problem:
# Step 1: Take each element in the list and round it up to the next integer.
# Step 2: Square the rounded element.
# Step 3: Add the result from step 2 to the total sum.
# Step 4: Repeat steps 1-3 for all elements in the list.
# Step 5: Return the total sum.

def sum_squares(lst):
    total = 0
    for i in lst:
        total += (int(i+0.5)**2)
    return total

# Testing the function
print(sum_squares([1,2,3])) # Expected output: 14
print(sum_squares([1,4,9])) # Expected output: 98
print(sum_squares([1,3,5,7])) # Expected output: 84
print(sum_squares([1.4,4.2,0])) # Expected output: 29
print(sum_squares([-2.4,1,1])) # Expected output: 6


































```