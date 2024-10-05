```
const concatenate = (strings) => strings.reduce((acc, current) => acc + current, '');
```
Explanation:

The `concatenate` function takes a list of strings as input and returns a single string that is the concatenation of all the input strings.

We use the `reduce` method to iterate over the input array of strings. The initial value of the accumulator (`acc`) is an empty string (`''`).

In each iteration, we concatenate the current string (`current`) to the accumulator (`acc`) using the `+` operator. The resulting string is returned as the new value of the accumulator.

Finally, the `reduce` method returns the final concatenated string. If the input array is empty, the `reduce` method returns the initial value of the accumulator, which is an empty string (`''`). This is consistent with the problem statement, which specifies that the output should be an empty string if the input array is empty.