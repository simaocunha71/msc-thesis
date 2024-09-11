```
def larg_nnum(lst,n):
    lst.sort()
    return lst[-n:]
```

This function first sorts the list in ascending order using the `sort()` method. Then, it uses list slicing to return the last `n` elements of the sorted list, which correspond to the `n` largest items. The `set()` function is used to convert the resulting list to a set, which eliminates any duplicate elements.

To test the function, the `assert` statement checks if the set of the function's output matches the expected set `[100,90]` for the input `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]` and `n=2`. If the assertion passes, it means that the function correctly returns the `n` largest items from the list.

Overall, this function provides a straightforward solution to the problem by utilizing built-in Python functions and concepts like sorting and list slicing.

Here is a step-by-step explanation of the code:

1. The `larg_nnum` function takes in two parameters: `lst` (the list of numbers) and `n` (the number of largest items to return).

2. The `lst.sort()` statement sorts the list in ascending order. This step is necessary to ensure that the largest items are at the end of the list.

3. The `lst[-n:]` expression uses list slicing to return the last `n` elements of the sorted list. These elements correspond to the `n` largest items.

4. The `return` statement returns the sliced list as the output of the function.

5. The `assert` statement is used to verify if the function's output matches the expected result. It checks if the set of the function's output (`set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))`) is equal to the expected set `set([100,90