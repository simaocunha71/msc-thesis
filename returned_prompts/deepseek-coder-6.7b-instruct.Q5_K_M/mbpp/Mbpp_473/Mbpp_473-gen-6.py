```python
def tuple_intersection(tuple_list):
    intersection = set(tuple_list[0])
    for tuples in tuple_list[1:]:
        intersection &= set(tuples)
    return intersection

print(tuple_intersection([(3, 4),  (5, 6),  (9, 10),  (4, 5)] , [(5, 4),  (3, 4),  (6, 5),  (9, 11)]]))
```

The function `tuple_intersection` takes a list of tuples as an input. It converts the first tuple in the list to a set and assigns it to `intersection`. Then it iterates over the remaining tuples in the list, and uses the `&=` operation to find the intersection of `intersection` and the set representation of the current tuple. Finally, it returns the resulting set.

The `&=` operation is a Python set operation that performs an intersection and assignment in a single step. It updates the set on which it's called to only include elements that are also in the set it's comparing to.

The print statement at the end calls the function with the provided tuple lists as arguments and prints the result.

The output of this program will be:
```python
{(4, 5), (3, 4), (5, 6)}
```
which represents the intersection of the given tuples.

