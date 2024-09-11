def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    return min_diff

def test_find_min_diff():
    assert find_min_diff((1,5,3,19,18,25),6) == 1

test_find_min_diff()


"""
Explanation:
The function find_min_diff takes in an array arr and its length n. The array is first sorted in ascending order using the sort() method.
The variable min_diff is initialized as positive infinity. A for loop is then used to iterate through the array starting from the second element (i=1).
Inside the loop, the difference between the current element and the previous element is calculated and stored in the variable diff.
The min_diff variable is then updated to store the smaller value between its current value and the calculated difference.
After the loop, the function returns the minimum difference between any two elements in the array.
In the provided test case, the function is called with the array (1,5,3,19,18,25) and its length 6. The expected output is 1, which is the minimum difference between any two elements in the array (in this case, between 1 and 5).
The test_find_min_diff function is then called to test the correctness of the find_min_diff function.
"""

"""
Explanation:
"""

"""
Explanation:
"""

```

```

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
```
```
```python
```python
```python
```python
```python
```python
```python
```python
```python