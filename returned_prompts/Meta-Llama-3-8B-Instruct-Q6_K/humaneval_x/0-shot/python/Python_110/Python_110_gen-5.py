```
def exchange(lst1, lst2):
    odd_nums_in_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    odd_nums_in_lst2 = sum(1 for num in lst2 if num % 2 != 0)
    
    if odd_nums_in_lst1 <= odd_nums_in_lst2:
        return "YES"
    else:
        return "NO"
```
In this solution, we first count the number of odd numbers in both lists using list comprehensions and the `sum` function. Then, we compare these counts. If the number of odd numbers in `lst1` is less than or equal to the number of odd numbers in `lst2`, it means that we can exchange elements between the two lists to make all the elements of `lst1` even, so we return "YES". Otherwise, we return "NO". 

This solution works because if we can make all elements of `lst1` even by exchanging elements with `lst2`, then the number of odd numbers in `lst1` must be less than or equal to the number of odd numbers in `lst2`, since we can always exchange an odd number from `lst2` with an odd number from `lst1`. If the number of odd numbers in `lst1` is greater than the number of odd numbers in `lst2`, then we cannot make all elements of `lst1` even by exchanging elements with `lst2`, so we return "NO". 

The time complexity of this solution is O(n), where n is the length of the input lists, since we are iterating over the elements of the lists once. The space complexity is O(1), since we are using a constant amount of space to store the counts of odd numbers. 