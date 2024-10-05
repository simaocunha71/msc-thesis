
def anti_shuffle(s):
    words = s.split(' ')
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))
    return ' '.join(words)

print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello !!!Wdlor'

# The function works by first splitting the input string into words.
# Then, for each word, it sorts the characters in ascending order based on their ASCII values and joins them back together.
# Finally, it joins the sorted words back together with a space between each word and returns the result.
# The order of the words and blank spaces is kept intact thanks to the use of the join and split functions.
<jupyter_output>
Hi
ehllo
Hello !!!Wdlor
<jupyter_text>
Question 3
<jupyter_code>
