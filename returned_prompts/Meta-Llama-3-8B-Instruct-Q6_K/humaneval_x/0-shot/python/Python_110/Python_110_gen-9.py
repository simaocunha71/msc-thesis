```
def exchange(lst1, lst2):
    even_nums = [x for x in lst1 if x % 2 == 0]
    odd_nums = [x for x in lst1 if x % 2 != 0]
    
    if len(odd_nums) > len(lst2):
        return "NO"
    
    for num in odd_nums:
        if num not in lst2:
            return "NO"
    
    return "YES"
```



Explanation:

The function `exchange(lst1, lst2)` takes two lists of numbers as input. It first separates the numbers in `lst1` into two lists: `even_nums` and `odd_nums`. 

It then checks if the number of odd numbers in `lst1` is greater than the length of `lst2`. If it is, it returns "NO", because it's impossible to make all elements of `lst1` even by exchanging elements with `lst2`.

Next, it checks if all odd numbers in `lst1` are present in `lst2`. If any odd number is not present in `lst2`, it returns "NO", because it's impossible to make all elements of `lst1` even by exchanging elements with `lst2`.

If all checks pass, it returns "YES", indicating that it's possible to make all elements of `lst1` even by exchanging elements with `lst2`. 

The function uses list comprehension to create the lists `even_nums` and `odd_nums`, and the `len` function to count the number of elements in these lists. The `in` operator is used to check if a number is present in `lst2`. 

This function assumes that the input lists will be non-empty. If the input lists can be empty, additional checks should be added to handle this case. 