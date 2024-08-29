def pack_consecutive_duplicates(lst):
    if not lst: return []
    result = [[lst[0]]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            result[-1].append(lst[i])
        else:
            result.append([lst[i]])
    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
<jupyter_output>
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
<jupyter_text>
Exercise 3: Write a function that checks if a string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
<jupyter_code>
