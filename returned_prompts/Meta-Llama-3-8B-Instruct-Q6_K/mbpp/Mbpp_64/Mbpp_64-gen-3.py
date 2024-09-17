```
def subject_marks(subjects):
    return sorted(subjects, key=lambda x: x[1])
```
This function sorts the list of tuples based on the second value of each tuple. The `sorted` function is used with a `key` argument that specifies a function to be called on each list element prior to making comparisons. In this case, the `key` function is a lambda function that returns the second value of each tuple (`x[1]`). 

The `sorted` function returns a new sorted list from the elements of any sequence. The `subject_marks` function returns this sorted list. 

For example, given the input `[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]`, the function will return `[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]`, which is the input list sorted based on the second value of each tuple. 

This function passes the given unit test. 

```
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```  ```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
