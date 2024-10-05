```
def histogram(test):
    test = test.split()
    if not test:
        return {}
    freq = {}
    for letter in test:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    max_count = max(freq.values())
    max_letters = [letter for letter, count in freq.items() if count == max_count]
    return {letter: max_count for letter in max_letters}
```


This function first splits the input string into a list of letters. If the list is empty, it returns an empty dictionary. Then, it creates a dictionary to store the frequency of each letter. It iterates over the list of letters and updates the frequency dictionary accordingly. 

After that, it finds the maximum frequency and creates a list of letters that have this maximum frequency. Finally, it returns a dictionary with these letters as keys and the maximum frequency as values. If there are multiple letters with the same maximum frequency, they are all included in the dictionary. If the input string is empty, the function returns an empty dictionary. 





Note: This solution assumes that the input string only contains lowercase letters and spaces. If the input string can contain other characters, you may need to add additional error handling.