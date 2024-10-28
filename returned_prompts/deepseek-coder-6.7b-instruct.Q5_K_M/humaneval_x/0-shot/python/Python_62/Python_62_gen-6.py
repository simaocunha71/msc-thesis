
```python
def derivative(xs: list):
    # remove the constant term
    xs = xs[1:]
    # multiply each coefficient by its corresponding power
    for i in range(len(xs)):
        xs[i] *= i+1
    return xs
```


```python
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivderivative([1, 2, 3]))  # [2, 6]
```

This function works by removing the constant term at the start of the polynomial (which is always 0, so doesn't affect the derivative), and then iteratively multiplies each coefficient by the power it corresponds to (starting at 1). This is the basic definition of the derivative of a polynomial.

I hope this helps ^_^

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