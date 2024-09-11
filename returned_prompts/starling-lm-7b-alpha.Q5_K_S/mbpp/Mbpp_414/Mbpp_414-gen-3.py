def overlapping(seq1, seq2):
    for i in seq1:
        if i in seq2:
            return True
    return False

# Testing the function
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
print("All tests passed")





"""
Overview:
This function checks if any number in the first sequence is present in the second one.
It does so by iterating over each value in the first sequence and checking if that number is in the second sequence.
If any number in the first sequence is found in the second one, the function returns True. Otherwise, it returns False.

Explanation:
The function takes two sequences, seq1 and seq2, as arguments. It then iterates over each value in seq1 using a for loop.
Inside the loop, it checks if the current value of the loop variable, i, is in seq2 using the in keyword.
If a value in seq1 is found in seq2, the function immediately returns True, indicating that the sequences have an overlapping value.
If no value in seq1 is found in seq2 after checking all values in seq1, the function returns False, indicating that the sequences do not have an overlapping value.

Testing:
The function is tested using the assert statement to ensure that it correctly determines whether the sequences have an overlapping value or not.
In the provided example, the function is called with the sequences [1,2,3,4,5] and [6,7,8,9]. Since no value in the first sequence is in the second sequence, the function should return False. The assert statement checks this result and prints "All tests passed" if the function's return value matches the expected result.
"""




















































































































