```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```


The function `find_tuples` takes a list of tuples and an integer `k` as inputs. It uses a list comprehension to iterate over the tuples and checks if all elements in each tuple are divisible by `k` using the `all` function and a generator expression. The `all` function returns `True` if all elements of the iterable are true. The function returns a list of tuples that have all elements divisible by `k`. 

The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` ensures that the function works correctly. It checks if the function returns the expected result when given a list of tuples and an integer `k`. 

The function works by iterating over each tuple in the list, and for each tuple, it checks if all elements are divisible by `k`. If all elements are divisible by `k`, the tuple is added to the result list. The function then returns the list of tuples that have all elements divisible by `k`. 





```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```


The function `find_tuples` takes a list of tuples and an integer `k` as inputs. It uses a list comprehension to iterate over the tuples and checks if all elements in each tuple are divisible by `k` using the `all` function and a generator expression. The `all` function returns `True` if all elements of the iterable are true. The function returns a list of tuples that have all elements divisible by `k`. 

The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` ensures that the function works correctly. It checks if the function returns the expected result when given a list of tuples and an integer `k`. 

The function works by iterating over each tuple in the list, and for each tuple, it checks if all elements are divisible by `k`. If all elements are divisible by `k`, the tuple is added to the result list. The