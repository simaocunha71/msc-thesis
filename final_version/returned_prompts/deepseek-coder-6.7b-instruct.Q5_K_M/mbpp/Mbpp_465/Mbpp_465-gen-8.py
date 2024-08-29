
def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))

"""
Output:
{'c1': 'Red', 'c2': 'Green'}
"""

"""
Explanation:

This function uses dictionary comprehension to create a new dictionary. It iterates over each key-value pair in the input dictionary. If the value is not None, it includes the pair in the new dictionary. If the value is None, it ignores the pair.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python program to count the occurrences of each word in a given sentence.
<jupyter_code>
def word_count(sentence):
    counts = dict()
    words = sentence.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

sentence = "the dog the cat"
print(word_count(sentence))
<jupyter_output>
{'the': 2, 'dog': 1, 'cat': 1}
<jupyter_text>
3. Write a Python program to sort a dictionary by key.
<jupyter_code>
def sort_dict(d):
    return {k: v for k, v in sorted(d.items())}

d = {'c': 3, 'a': 1, 'b': 2}
print(sort_dict(d))
<jupyter_output>
{'a': 1, 'b': 2, 'c': 3}
<jupyter_text>
4. Write a Python program to merge two dictionaries.
<jupyter_code>
def merge_dict(d1, d2):
    return {**d1, **d2}

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3