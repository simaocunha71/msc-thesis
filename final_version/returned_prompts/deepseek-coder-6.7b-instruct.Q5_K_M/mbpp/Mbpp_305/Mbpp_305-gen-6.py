
def start_withp(lst):
    result = []
    for item in lst:
        words = item.split()
        for word in words:
            if word.lower().startswith('p'):
                result.append(word)
    return tuple(result)

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

#Output: ('Python', 'PHP')

"""
This function works by iterating over each string in the given list. It splits each string into its constituent words using the split() method. Then it checks if each word starts with the letter 'p'. If the word starts with 'p', it is appended to the result list. Finally, the function returns the result list as a tuple.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
