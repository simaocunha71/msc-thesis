
def max_occurrences(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    max_frequency = max(count_dict.values())
    for key, value in count_dict.items():
        if value == max_frequency:
            return key

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))
<jupyter_output>
2
<jupyter_text>
