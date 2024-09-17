```
def freq_count(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
```


The function `freq_count` takes a list as input and returns a dictionary where the keys are the elements in the list and the values are their corresponding frequencies. It does this by iterating over the list, and for each element, it checks if the element is already a key in the dictionary. If it is, it increments the value by 1; if it's not, it adds the element as a new key with a value of 1.

For example, if we call `freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])`, the function will return `({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})`, which is the frequency count of each element in the list. This is also the expected output according to the unit test. 