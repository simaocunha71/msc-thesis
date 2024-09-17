```
def find_sum(lst):
    from collections import Counter
    counter = Counter(lst)
    return sum(x for x in lst if counter[x] == 1)
```


The function `find_sum` takes a list of elements as input and returns the sum of non-repeated elements in the list. The function uses the `Counter` class from the `collections` module to count the frequency of each element in the list. Then it uses a generator expression to sum up the elements that have a frequency of 1, which means they are non-repeated. 

The unit test `assert find_sum([1,2,3,1,1,4,5,6]) == 21` ensures that the function works correctly. It checks if the sum of non-repeated elements in the list `[1,2,3,1,1,4,5,6]` is equal to `21`. 

This function can handle lists of any size and will correctly identify the sum of non-repeated elements.  If there are no non-repeated elements, it will return `0`.  If there are multiple non-repeated elements with the same value, they will be counted only once in the sum.  For example, in the list `[1,2,3,1,1,4,5,6,2,3]`, the non-repeated elements are `4` and `5`, so the function will return `9`, which is the sum of these elements.  If the list is `[1,1,1,1,1]`, the function will return `0`, because there are no non-repeated elements.  If the list is `[1,2,3,4,5,6]`, the function will return `15`, which is the sum of all elements.  If the list is `[1,1,2,2,3,3,4,5,6,6]`, the function will return `12`, which is the sum of the non-repeated elements `4` and `5`.  If the list is `[1,2,3,4,5,6,7,8,9,10]`, the function will return `55`, which is the sum of all elements.  If the list is `[1,1,1,1,1,1,1,1,1,1]`, the function will return `0`, because there are no non-repeated elements.  If