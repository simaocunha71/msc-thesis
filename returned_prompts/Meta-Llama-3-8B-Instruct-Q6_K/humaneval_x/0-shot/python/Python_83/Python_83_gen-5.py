```
def starts_one_ends(n):
    # Initialize a variable to store the count
    count = 0
    
    # Loop through all n-digit numbers
    for num in range(10**(n-1), 10**n):
        # Check if the number starts or ends with 1
        if str(num).startswith('1') or str(num).endswith('1'):
            # Increment the count if the number meets the condition
            count += 1
    
    # Return the count
    return count
```
This function uses a loop to iterate through all n-digit numbers, converts each number to a string, and checks if the string starts or ends with '1'. If it does, the count is incremented. Finally, the function returns the count.