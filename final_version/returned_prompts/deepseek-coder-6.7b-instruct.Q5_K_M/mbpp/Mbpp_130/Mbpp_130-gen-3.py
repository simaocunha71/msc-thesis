def max_occurrences(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    max_freq = max(count_dict.values())
    for key, value in count_dict.items():
        if value == max_freq:
            return key

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))

# Output: 2
<jupyter_output>
2
<jupyter_text>
Question 4: Write a function to find the largest and smallest number in a given list. The function should return a tuple containing the min and max numbers.assert largest_and_smallest([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==(1, 9)
<jupyter_code>
# Answer:

def largest_and_smallest(lst):
    return min(lst), max(lst)

print(largest_and_smallest([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))

# Output: (1, 9)
<jupyter_output>
(1, 9)
<jupyter_text>
Question 5: Write a function to find the median of a given list. The function should return the median value.assert median([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==4.5
<jupyter_code>
# Answer:

def median(lst):
    n = len(lst)
    s = sorted(