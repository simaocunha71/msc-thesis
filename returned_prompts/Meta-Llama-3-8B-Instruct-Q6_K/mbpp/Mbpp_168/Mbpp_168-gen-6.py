```
def frequency(lst, target):
    return lst.count(target)
```


Here, the function `frequency` takes two parameters: a list `lst` and a target number `target`. It returns the number of occurrences of `target` in `lst` using the built-in `count` method of lists. 

The unit test `assert frequency([1,2,3], 4) == 0` ensures that the function returns 0 when the target number is not in the list. 

This function is case-sensitive and will count the occurrences of the exact target number, including duplicates. If you want to count occurrences of any number that is equal to the target (regardless of duplicates), you can convert the list to a set and then back to a list to remove duplicates, and then use the `count` method. For example: `return list(set(lst)).count(target)`. However, this would not preserve the original order of the list. If you need to preserve the order, you could use a dictionary to keep track of the counts, like so: `from collections import Counter; return Counter(lst)[target]`. 

Remember that the `count` method has a time complexity of O(n), where n is the length of the list, so it may not be efficient for very large lists. If you need to count the occurrences of a number in a very large list, you may want to consider using a more efficient algorithm, such as a hash table.  However, for small to medium-sized lists, the `count` method should be sufficient.  If you're working with a list of numbers and you need to count the occurrences of each unique number, you might consider using the `Counter` class from the `collections` module, like so: `from collections import Counter; counter = Counter(lst); return counter[target]`. This has a time complexity of O(n) but is generally faster than using the `count` method.  It also returns the total count of the target number, not just the first occurrence.  If you want to count the occurrences of the first occurrence of the target number, you'll need to use a different approach.  For example, you could use a loop to iterate over the list and keep track of the count manually.  However, this would be less efficient than using the `count` method or the `Counter` class.  It's generally a good idea to use the most efficient method that meets your needs.  In this case, since the problem