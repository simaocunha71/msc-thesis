def count_charac(s):
    count = 0
    for i in s:
        count += 1
    return count

print(count_charac("python programming"))

#or using built-in function
def count_charac(s):
    return len(s)

print(count_charac("python programming"))

#or using lambda function
count_charac = lambda s: len(s)
print(count_charac("python programming"))

#or using map function
count_charac = lambda s: sum(map(lambda x: 1, s))
print(count_charac("python programming"))
<jupyter_output>
18
18
18
18
<jupyter_text>
1.13. Write a Python program to count the number of words in a string.
<jupyter_code>
