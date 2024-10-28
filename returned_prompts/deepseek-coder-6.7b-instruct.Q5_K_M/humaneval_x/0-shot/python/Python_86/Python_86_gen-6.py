
    s_list = s.split()
    new_s_list = []
    for word in s_list:
        new_word = ''.join(sorted(word))
        new_s_list.append(new_word)
    return ' '.join(new_s_list)

# Test cases
print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello  !!!Wdlor'

"""
This function works by splitting the input string into a list of words, then for each word in the list, it sorts the characters in ascending order based on their ascii value and joins them together into a new word. The new words are then joined back together with spaces in between into a new string.
"""
<jupyter_output>
Hi
ehllo
Hello  !!!Wdlor
<jupyter_text>
Task 2
<jupyter_code>
