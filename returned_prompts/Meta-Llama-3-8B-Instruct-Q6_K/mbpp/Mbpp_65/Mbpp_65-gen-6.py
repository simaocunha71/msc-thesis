You can use recursion to solve this problem. Here's a Python function that does that:

```python
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total
```

This function goes through each element in the list. If the element is a list itself, it calls itself with that list and adds the result to the total. If the element is not a list, it simply adds it to the total. The function keeps doing this until it has gone through all elements in the list. The base case for the recursion is when the function encounters a non-list element, at which point it stops calling itself and starts returning results up the call stack.

The unit test you provided, `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21`, shows that this function works correctly. The expected result is 21, which is the sum of the elements in the list: 1 + 2 + 3 + 4 + 5 + 6 = 21.  This function will work with lists of arbitrary depth, not just two levels deep. For example, `recursive_list_sum([1, 2, [3, 4, [5, 6]]])` would also return 21.  This is because it uses recursion, which allows it to handle lists of arbitrary depth.  Without recursion, you would need to write a loop that checks if each element is a list, and if so, calls itself with that list.  This would make the function much more complicated and harder to read.  Recursion is a simple and elegant way to solve this problem.  It's a good example of how recursion can be used to solve a problem that would be difficult or impossible to solve with a loop.  It's also a good example of how recursion can make code more readable and maintainable.  The function is easy to understand, even though it's solving a complex problem.  This is because it's using a simple and natural way to solve the problem.  It's not trying to use a loop to solve the problem, which would make the code more complicated and harder to read.  Instead, it's using recursion, which is a natural and simple way to solve this type of problem.  This makes the code easy to understand and maintain.  It's also a good