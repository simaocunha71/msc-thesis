```
def subject_marks(subjects):
    return sorted(subjects, key=lambda x: x[1])
```
This function uses the built-in `sorted` function to sort the list of tuples. The `key` parameter of the `sorted` function is a function that takes a tuple and returns its second value, which is used for sorting. The `lambda` function is used to define this key function. The `sorted` function returns a new sorted list and leaves the original list unchanged. 

For example, if the input list is `[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]`, the function will return `[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]`. 

The unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` ensures that the function works correctly. 
```
```python
python
def subject_marks(subjects):
    return sorted(subjects, key=lambda x: x[1])

assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python
```python
python