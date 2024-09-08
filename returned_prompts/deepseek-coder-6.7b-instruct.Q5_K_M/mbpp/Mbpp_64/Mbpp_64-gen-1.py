You can use the built-in function sorted() along with a lambda function to sort the list by the second element of each tuple.

```python
def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])
```

You can then call this function with the list of tuples as an argument. The function will return the list sorted by the second element of each tuple.

```python
print(subject_marks([('English', 88),  ('Science', 90