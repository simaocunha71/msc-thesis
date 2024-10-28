```
def sum_of_digits(lst):
    return sum(sum(map(int, str(x))) for x in lst)
```
This function works by using a generator expression to convert each number in the list to a string, then to a sequence of digits (by mapping `int` over the string), then to the sum of those digits (by summing the sequence), and finally to the total sum of all those sums (by summing the results). The unit test `assert sum_of_digits([10,2,56])==14` passes. 
```
print(sum_of_digits([10,2,56]))  # Output: 14
``` 





