```
def freq_count(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
```


Explanation:
The function `freq_count` takes a list `lst` as input and returns a dictionary where the keys are the unique elements from the list and the values are their corresponding frequencies.

We iterate over each item in the list. If the item is already a key in the dictionary, we increment its value by 1. If the item is not a key in the dictionary, we add it with a value of 1. This way, we keep track of the frequency of each item in the list.

Finally, we return the dictionary containing the frequency of all elements in the list.

The unit test `assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})` ensures that the function works correctly. It checks if the output of the function is equal to the expected output for the given input. If the function is working correctly, the assertion will pass. Otherwise, it will raise an AssertionError.