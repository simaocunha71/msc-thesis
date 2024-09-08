def Diff(list1, list2):
    return [i for i in list1 if i not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

# Output: [10, 20, 30, 15]

"""
The function Diff() takes two lists as input. It uses list comprehension to iterate over each element in list1, 
and if that element is not in list2, it includes it in the output list. The output list is then returned by the function.
"""

# Solution by: Tushar Kumar

# Thank You
<jupyter_output>
<empty_output>
<jupyter_text>
Q3: Write a Python function to calculate the frequency of each word in a text file.
<jupyter_code>
# Python program to calculate the frequency of each word in a text file

def word_freq(file):
    with open(file, 'r') as f:
        text = f.read().lower()
        words = text.split()
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        return freq

# Test the function
print(word_freq('text.txt'))

# Solution by: Tushar Kumar

# Thank You
<jupyter_output>
<empty_output>
<jupyter_text>
Q4: Write a Python function to find the square of each number in a list.
<jupyter_code>
# Python program to find the square of each number in a list

def square_numbers(lst):
    return [num ** 2 for num in lst]

# Test the function
print(square_numbers([1, 2, 3, 4, 5]))

# Solution by: Tushar Kumar

# Thank You
<jupyter_output>
