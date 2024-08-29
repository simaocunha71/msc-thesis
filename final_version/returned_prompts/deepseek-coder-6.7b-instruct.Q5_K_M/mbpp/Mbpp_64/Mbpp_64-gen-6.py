```python
def subject_marks(lst):
    lst.sort(key=lambda x: x[1])
    return lst

print(subject_marks([('English', 88),  ('Science', 90),  ('Maths', 97),  ('Social sciences', 82)]))
```

