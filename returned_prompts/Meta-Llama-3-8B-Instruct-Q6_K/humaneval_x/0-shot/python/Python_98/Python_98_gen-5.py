```
def count_upper(s):
    return sum(1 for i in range(0, len(s), 2) if s[i].upper() in 'AEIOU')
```


This function works by iterating over the indices of the string in steps of 2 (i.e., the even indices), and for each index, checking if the character at that index is an uppercase vowel. The `sum` function is used to count the number of True values in the generator expression. The `upper` method is used to convert the character to uppercase before checking if it's a vowel, and the `in` operator is used to check if the character is in the string 'AEIOU'. If the character is a vowel and the index is even, the function counts it. The result is the number of uppercase vowels in even indices.