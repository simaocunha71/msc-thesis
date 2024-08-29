
def max_occurrences(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    max_freq = max(frequency_dict.values())
    for key, value in frequency_dict.items():
        if value == max_freq:
            return key

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))  # Output: 2

"""
Explanation:
The function 'max_occurrences' works by first creating a dictionary 'frequency_dict' where the keys are the elements in the list and the values are their corresponding frequencies. It then finds the maximum frequency 'max_freq'. In the end, it returns the key corresponding to the maximum frequency.
"""
<jupyter_output>
2
<jupyter_text>
3. Write a Python program to find the second largest number in a list.
<jupyter_code>
