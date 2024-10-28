Using `_, v` in a loop allows you to ignore the index of the iteration. In this case, since the index is not used in the loop's body, it's more efficient to ignore it to avoid the overhead of calculating the index for each iteration.

Here's a breakdown of the code:

- The `for`, `range` loop iterates over each element in the `stringList` slice. For each iteration, the loop assigns the index and the value to the variables `_` and `v`, respectively.
- The `_` variable is used to explicitly ignore the index, which is not used in the loop's body. This is a common practice when the index is not needed in the loop's logic.
- The `v` variable holds the value of each element from the `stringList` slice, allowing us to check if the substring is present in that element.

Using `_, v` instead of `v`, `v` is a matter of preference and readability. Some programmers find it more clear to explicitly ignore the index, while others may find it unnecessary.

Overall, the `FilterBySubstring` function filters the input list of strings based on whether they contain the given substring. The function uses a for loop with `_, v` to iterate over the `stringList` slice and checks if the substring is present in each element using `strings.Contains()`. The elements that contain the substring are appended to the `res` slice, which is then returned as the result.

I hope this explanation helps! Let me know if you have any more questions.

Here's a breakdown of the code:

The `for`, `range` loop iterates over each element in the `stringList` slice. For each iteration, the loop assigns the index and the value to the variables `_` and `v`, respectively.

The `_` variable is used to explicitly ignore the index, which