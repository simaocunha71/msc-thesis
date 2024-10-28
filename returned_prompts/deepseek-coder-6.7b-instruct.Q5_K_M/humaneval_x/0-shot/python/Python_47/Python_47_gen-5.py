
    l.sort()
    n = len(l)
    
    if n % 2 == 0:
        return (l[n//2-1] + l[n//2]) / 2
    else:
        return l[n//2]
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Exercise 2**: Write a function called `mode` that takes a list of numbers and returns the most frequently occurring number in the list. In case of a tie, return the smallest number. If the list is empty, return `None`.```python