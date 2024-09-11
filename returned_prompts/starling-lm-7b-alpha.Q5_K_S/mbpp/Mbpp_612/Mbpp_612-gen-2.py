```
def merge(l):
    l1 = []
    l2 = []
    for i in l:
        l1.append(i[0])
        l2.append(i[1])
    return [l1, l2]
```

merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) # returns [['x', 'a', 'm'], ['y', 'b', 'n']]

Explanation:
The merge function takes a list of lists as an input. It initializes two empty lists, l1 and l2. It then iterates through the input list, appending the first element of each sublist to l1 and the second element of each sublist to l2. Finally, it returns a list containing l1 and l2, in that order.

In the provided example, merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) is called, which returns [['x', 'a', 'm'], ['y', 'b', 'n']]. This means that the first element of each sublist in the original list is added to l1 in the order they appear, resulting in ['x', 'a', 'm'], and the second element of each sublist is added to l2 in the order they appear, resulting in ['y', 'b', 'n'].

To test the function, you can use the assert statement to verify if the output of the function matches the expected output. In this case, assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']] ensures that the function returns the correct result.

Overall, this function provides a way to merge two elements from each sublist in a list of lists into two separate lists, while maintaining the order of the original sublists.

Here are some additional test cases you can use to further verify the function's correctness:

merge([['z', 'c'], ['d', 'e'], ['f', 'g']]) == [['z', 'd', 'f'], ['c', 'e', 'g']]
merge([['h', 'i'], ['j', 'k'], ['l', '