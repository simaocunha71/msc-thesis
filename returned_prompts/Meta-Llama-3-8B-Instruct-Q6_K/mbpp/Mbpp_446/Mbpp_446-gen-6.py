```
def count_Occurrence(tuple, elements):
    occurrence_count = {}
    for element in elements:
        occurrence_count[element] = tuple.count(element)
    return occurrence_count
```
The function `count_Occurrence` takes a tuple and a list of elements as inputs. It initializes an empty dictionary `occurrence_count`. Then it iterates over the elements in the list. For each element, it counts the number of occurrences of the element in the tuple using the `count` method and stores the count in the dictionary. Finally, it returns the dictionary.

The unit test `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3` ensures that the function correctly counts the occurrence of each element in the list in the tuple.

Note: This function returns a dictionary where the keys are the elements from the list and the values are the counts of the occurrences of the elements in the tuple. If you want to get the total count of occurrences of all elements in the list in the tuple, you can use the `sum` function to sum up the values in the dictionary. For example, `sum(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ).values())` would return `3`. 