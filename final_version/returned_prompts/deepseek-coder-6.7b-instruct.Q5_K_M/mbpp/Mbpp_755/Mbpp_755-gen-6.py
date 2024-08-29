
def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))

"""
The function works by initializing two variables, m1 and m2, to positive infinity. Then it iterates through the list of numbers. If it encounters a number that is smaller than or equal to m1, it updates m1 and m2 with the new number. If it encounters a number that is between m1 and m2, it updates m2 with the new number. At the end of the function, m2 will contain the second smallest number in the list.
"""
<jupyter_output>
-2
<jupyter_text>
8. Write a Python program to find the length of a string.
<jupyter_code>
str = "Hello, World!"
print(len(str))
<jupyter_output>
13
<jupyter_text>
9. Write a Python program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
<jupyter_code>
items = input("Enter comma-separated sequence of words:")
words = [word for word in items.split(",")]
print(",".join(sorted(words)))
<jupyter_output>
Enter comma-separated sequence of words:red, green, blue, yellow
blue, green, red, yellow
<jupyter_text>
10. Write a Python program to count the occurrences of each word in a given sentence.
<jupyter_code>
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print