"""
In order to get all the possible sequences, we can start by initializing the first element of the sequence as 2. This is because the number must be at least twice the previous element. We then initialize a variable to keep track of the number of sequences. We can then use a loop that will run n - 1 times to get all the remaining elements of the sequence. In each iteration of the loop, we can add the number 2 to the last element of the sequence. We can then add the last element of the sequence to the total number of sequences. After the loop is finished, we can return the total number of sequences. We can use recursion to solve this problem. To do this, we can define a function called get_total_number_of_sequences that takes in the total number of sequences, the length of the sequence, and the maximum number of the sequence as parameters. We can then check if the length of the sequence is equal to 0. If it is, we can return the total number of sequences. If not, we can call the function again with the updated parameters to get the total number of sequences for the next element of the sequence. We can add the total number of sequences for the next element of the sequence to the total number of sequences for the current element of the sequence. We can then return the total number of sequences. We can use the assert statement to test the function and check if it returns the correct result for the given input."""

# Python code
def get_total_number_of_sequences(m, n):
    def helper(total_sequences, length, max_sequence):
        if length == 0:
            return total_sequences
        else:
            return helper(total_sequences + max_sequence, length - 1, m)
    return helper(0, n, 2)

# Testing the function
assert get_total_number_of_sequences(10, 4) == 4

# End of Python code

"""
The provided Python code defines a function called get_total_number_of_sequences that takes in two positive integers m and n as input. The function uses recursion to calculate the total number of possible sequences of length n, where each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m. The