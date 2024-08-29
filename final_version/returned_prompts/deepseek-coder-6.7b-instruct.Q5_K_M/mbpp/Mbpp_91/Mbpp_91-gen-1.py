
def find_nth_occurrence(string, substring, n):
    count = 0
    pos = 0
    while count < n:
        pos = string.find(substring, pos)
        if pos == -1:
            return -1
        pos += 1
        count += 1
    return pos - 1

print(find_nth_occurrence("Hello world, world is beautiful, isn't world wonderful", "world", 2)) # 28
print(find_nth_occurrence("Hello world, world is beautiful, isn't world wonderful", "world", 1)) # 6
print(find_nth_occurrence("Hello world, world is beautiful, isn't world wonderful", "world", 3)) # 33
<jupyter_output>
28
6
33
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a function to count the number of occurre