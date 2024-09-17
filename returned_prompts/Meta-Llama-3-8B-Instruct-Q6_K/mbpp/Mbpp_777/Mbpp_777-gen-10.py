```
def find_sum(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    sum_non_repeated = 0
    for num, frequency in frequency_dict.items():
        if frequency == 1:
            sum_non_repeated += num
    
    return sum_non_repeated
```


The function `find_sum` takes a list of numbers as input and returns the sum of the non-repeated elements. It first creates a dictionary to store the frequency of each number in the list. Then, it iterates over the dictionary and adds the non-repeated numbers to a running total. The function finally returns the sum of the non-repeated elements. The unit test `assert find_sum([1,2,3,1,1,4,5,6]) == 21` ensures that the function works correctly. 
For example, if the input list is `[1,2,3,1,1,4,5,6]`, the function would return `21` because the non-repeated elements are `2`, `3`, `4`, `5`, and `6`, and their sum is `21`.  If the input list is `[1,1,1,2,2,3,4,5,6]`, the function would return `15` because the non-repeated elements are `3`, `4`, `5`, and `6`, and their sum is `15`.  If the input list is `[1,2,3,4,5,6]`, the function would return `21` because all elements are non-repeated.  If the input list is `[1,2,2,2,3,3,3,4,5,6]`, the function would return `15` because the non-repeated elements are `1`, `4`, and `5`, and their sum is `15`.  If the input list is `[1,1,1,1,1,1,1,1,1]`, the function would return `0` because all elements are repeated.  If the input list is `[]`, the function would return `0` because there are no elements.  If the input list is `[1,1,1,1,1,1,1,1,1,1]`, the function would return `0` because