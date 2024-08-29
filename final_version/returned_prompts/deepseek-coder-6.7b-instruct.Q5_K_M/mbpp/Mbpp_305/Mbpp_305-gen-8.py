
def start_withp(words):
    for word in words:
        if word.startswith('p'):
            return word.split()[0], word.split()[1]

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

# Solution 2:
# Using list comprehension

def start_withp(words):
    return tuple(word.split()[i] for word in words for i in range(2) if word.startswith('p', i))

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

Both of the above solutions will return the expected result ('Python', 'PHP').

The first solution is more readable and easier to understand. The second solution is more efficient and uses less memory.

The second solution uses a generator expression, which is a high performance, memory efficient generalization of list comprehensions and generators. It is also more efficient because it doesn't need to create a temporary list to store the results.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
"""
