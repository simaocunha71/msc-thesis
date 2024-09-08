
def len_long(words):
    return max(len(word) for word in words)

print(len_long(["python","PHP","bigdata"]))

#or
def len_long(words):
    return max(words, key=len)

print(len_long(["python","PHP","bigdata"]))
<jupyter_output>
7
python
<jupyter_text>
Q2. Write a python function to find the second largest number in the list.
<jupyter_code>
