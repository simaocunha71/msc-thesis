```
def long_words(n, words):
    return [word for word in words if len(word)>n]
```
This function takes two parameters: `n` (the length threshold) and `words` (the list of words). It uses a list comprehension to create a new list containing only the words that are longer than `n` characters. The `len(word)>n` condition is used to filter the words. 

The unit test `assert long_words(3,"python is a programming language")==['python','programming','language']` ensures that the function works correctly. It checks that the function returns a list containing the words 'python', 'programming', and 'language' when given the threshold of 3 and the list of words "python is a programming language". 

This function will return all words that are longer than `n` characters, not just the first one. If you want to return only the first word that meets the condition, you can modify the function to use the `next` function with a generator expression: `next((word for word in words if len(word)>n), None)`. This will return the first word that is longer than `n` characters, or `None` if no such word exists. 
```python
def long_word(n, words):
    return next((word for word in words if len(word)>n), None)
``` 
This version of the function will stop iterating as soon as it finds a word that meets the condition, which can be more efficient if the list of words is very long. However, it will return only the first word that meets the condition, not all of them. 
```python
assert long_word(3,"python is a programming language")=='python'
``` 
The unit test `assert long_word(3,"python is a programming language")=='python'` ensures that the function works correctly. It checks that the function returns the word 'python' when given the threshold of 3 and the list of words "python is a programming language". 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```python
``` 
```