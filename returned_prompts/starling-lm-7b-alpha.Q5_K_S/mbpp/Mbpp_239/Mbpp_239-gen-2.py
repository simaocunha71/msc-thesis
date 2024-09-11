```
def get_total_number_of_sequences(m, n):
    # Initialize result
    result = 0

    # Initialize sequence with 1
    seq = [1]

    # Initialize count of valid sequences
    count = 0

    # Generate all sequences of length n
    while len(seq) < n:
        # Generate next number in the sequence
        new_num = 2 * seq[-1]

        # Check if new_num is valid
        if new_num <= m:
            # Add new_num to sequence
            seq.append(new_num)
            # Increment count
            count += 1
        else:
            # Backtrack and find a valid new_num
            while len(seq) > 0 and new_num > m:
                # Remove last number from sequence
                seq.pop()
                # Reduce count
                count -= 1
                # Generate new_num again
                new_num = 2 * seq[-1]
            # Add new_num to sequence
            seq.append(new_num)
            # Increment count
            count += 1

    # Return count of valid sequences
    result = count

    return result
```

Here's a function that solves the problem. It first initializes an empty result variable and a sequence with a single element, 1. It also initializes a count variable to keep track of the number of valid sequences. 

The function then enters a while loop, which continues until the length of the sequence is equal to the input n. Inside the loop, it generates the next number in the sequence by multiplying the last element of the sequence by 2. 

If the new number is less than or equal to the input m, it is added to the sequence and the count is incremented. Otherwise, the function backtracks by removing the last number from the sequence and reducing the count until it finds a valid new number. 

Finally, the function returns the count of valid sequences. 

You can test the function with the provided assert statement to ensure it works correctly.

The time complexity of this solution is O(n * log(m)), where n is the length of the sequence and m is