```
def sum_list(a, b):
    return [x+y for x,y in zip(a,b)]
```


Explanation:
The problem asks to create a function that takes two lists of numbers as input and returns a new list where each element is the sum of the corresponding elements from the input lists. For example, if the input lists are [10,20,30] and [15,25,35], the output should be [25,45,65].

The solution uses a list comprehension and the built-in zip function. The zip function takes two lists and returns an iterator that aggregates elements based on the iterables passed, making an iterator that returns tuples based on the iterables passed. In this case, it pairs each element from the two lists together.

The list comprehension then sums each pair of elements and returns the result as a new list. This is a concise and efficient way to solve the problem. The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` confirms that the function works as expected.