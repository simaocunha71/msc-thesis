```python
def anti_shuffle(s):
    def sort_string(word):
        return ''.join(sorted(word))

    return ' '.join(sort_string(word) for word in s.split(' '))

print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello !!!Wdlor'
```
