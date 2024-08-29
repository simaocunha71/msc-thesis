def freq_count(lst):
    return {i: lst.count(i) for i in lst}


print(freq_dict([10,10,10,10,20,20,20,20,40,40,50,50,30]))
<jupyter_output>
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
<jupyter_text>
Solution 2: Using Python's built-in collections module
<jupyter_code>
from collections import Counter

def freq_count(lst):
    return dict(Counter(lst))


print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
<jupyter_output>
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
<jupyter_text>
Solution 3: Using defaultdict from Python's built-in collections module
<jupyter_code>
from collections import defaultdict

def freq_count(lst):
    freq_dict = defaultdict(int)
    for num in lst:
        freq_dict[num] += 1
    return freq_dict


print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
<jupyter_output>
defaultdict(<class 'int'>, {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
<jupyter_text>
All three solutions will give the same output. However, the first solution is using list.count() method which is less time-efficient for large lists.