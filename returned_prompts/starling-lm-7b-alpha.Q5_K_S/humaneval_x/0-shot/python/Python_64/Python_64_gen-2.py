
def vowels_count(s):
    vowels = "aeiouy"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

if __name__ == "__main__":
    print(vowels_count("abcde"))
    print(vowels_count("ACEDY"))


# Made By Mostafa_Khaled
```
        

# Here are some test cases you can use to check your implementation:

```python
print(vowels_count("abcde"))  # Should print: 2
print(vowels_count("ACEDY"))  # Should print: 3
```
        
        
# Note that this problem is quite simple, and you can solve it with a simple loop over the string, and increment a counter every time we find a vowel (which are the letters `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and `'y'`).
```

```
            
        
# Here are some test cases you can use to check your implementation:

```python
print(vowels_count("abcde"))  # Should print: 2
print(vowels_count("ACEDY"))  # Should print: 3
```
```