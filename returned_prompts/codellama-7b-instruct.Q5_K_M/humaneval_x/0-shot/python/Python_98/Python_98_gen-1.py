
def count_upper(s):
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            count += 1
    return count

This is one of the most straightforward ways to solve the problem.

It would be interesting to see a more pythonic way to solve this problem.
