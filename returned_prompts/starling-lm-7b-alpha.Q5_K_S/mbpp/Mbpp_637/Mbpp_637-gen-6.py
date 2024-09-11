To solve this problem you need to calculate the average of the two numbers. If the average of the two numbers is equal to the smaller number, then there is no profit, no loss. Otherwise, there is either a profit or a loss.

Here's a step-by-step guide on how to solve this problem.

First, define the function noprofit_noloss:

```python
def noprofit_noloss(amount1, amount2):
```

Then, calculate the average of the two amounts:

```python
average = (amount1 + amount2) / 2
```

Now, compare the average to both amounts to see if they are equal:

```python
if average == amount1 and average == amount2:
```

If they are equal, return True:

```python
    return True
```

If they are not equal, return False:

```python
else:
    return False
```

So the full function will look like this:

```python
def noprofit_noloss(amount1, amount2):
    average = (amount1 + amount2) / 2
    if average == amount1 and average == amount2:
        return True
    else:
        return False
```

You can call this function with two numbers to check if there is no profit and no loss:

```python
print(noprofit_noloss(1500, 1200))  # This will print False
```

This will return False because 1200 is not equal to the average of 1500 and 1200 (1350), indicating there is either a profit or a loss.

Here are some more examples:

```python
print(noprofit_noloss(100, 100))  # This will print True
print(noprofit_noloss(200, 150))  # This will print False
```

These will return True and False respectively because the average of the two numbers is equal to the smaller number in the first example, but not in the second.

