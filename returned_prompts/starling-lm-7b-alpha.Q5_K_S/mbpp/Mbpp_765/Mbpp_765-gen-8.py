"""
The nth polite number is defined as the smallest number such that no digit in the number is repeated in the number itself. For example, the first polite number is 1, the second is 2, and so on. Here are the first few polite numbers: 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, …

To find the nth polite number, you can start with the first polite number, 1, and keep adding the smallest number that doesn't have any digit repeated in it. Here's a step-by-step breakdown of the process:

1. Start with the first polite number, 1.
2. Check if the current number is greater than or equal to n. If it is, return the current number as the nth polite number.
3. If the current number is less than n, find the smallest number that doesn't have any digit repeated in it by starting from the next number (current number + 1) and incrementing it until you find a number that doesn't have any repeated digits. Add this number to the list of polite numbers.
4. Repeat steps 2 and 3 until you find the nth polite number.

Here's a Python function that implements the above steps to find the nth polite number:

def find_nth_polite_number(n):
    polite_numbers = [i for i in range(1, n + 1)]
    for i in range(n + 1, len(polite_numbers)):
        if len(set(str(polite_numbers[i]))) == len(str(polite_numbers[i])):
            polite_numbers.append(polite_numbers[i])
        else:
            j = i + 1
            while len(set(str(j))) != len(str(j)):
                j += 1
            polite_numbers.append(j)
    return polite_numbers[n]

You can use the function like this:

print(find_nth_polite_number(7))  # Output: 11
"""

def is_polite(n):
    return len(set(