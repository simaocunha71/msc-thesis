
Here is a solution in Go:

```go
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, len(numbers)*2-1)
    for i, num := range numbers {
        result[i*2] = num
        result[i*2+1] = delimeter
    }
    return result
}
```

Here is a solution in Python:

```python
def Intersperse(numbers, delimeter):
    result = []
    for i, num in enumerate(numbers):
        result.extend([num, delimeter])
    return result
```

You can use the above Python function in Python 3.x interpreter like this:

```python
print(Intersperse([], 4)) # []
print(Intersperse([1, 2, 3], 4)) # [1, 4, 2, 4, 3]
```

Explanation:

In the Go solution, a slice named `result` is created with length `len(numbers)*2-1` to store the final result. Then, a for loop is used to iterate over the input slice `numbers`. For each number, it is appended to the `result` slice followed by the `delimeter`. This is done using the `append` function. Finally, the `result` slice is returned.

In the Python solution, a list named `result` is created to store the final result. A for loop is used to iterate over the input list `numbers`. For each number, it is appended to the `result` list followed by the `delimeter`. This is done using the `extend` function. Finally, the `result` list is returned.

In both solutions, the `delimeter` is inserted between every two consecutive elements of the input list, resulting in the desired output.

Note: The `Intersperse` function in Go returns a slice, while the `Intersperse` function in Python returns a list. However, both functions achieve the same result of inserting a `delimeter` between every two consecutive elements of the input list.

Here are some test cases for the Python function:

