
To find the maximum element in a list of integers, you can use the following algorithm:

1. Initialize a variable `max` to the first element of the list.
2. Iterate through the list starting from the second element.
3. For each element in the list, compare it with the current maximum `max`.
4. If the element is greater than the current maximum `max`, update the value of `max` to the element.
5. Repeat steps 3 and 4 until all elements in the list have been checked.
6. Return the final value of `max`, which will be the maximum element in the list.

Here's an example implementation of the algorithm in Go:

```go
func MaxElement(l []int) int {
    max := l[0]
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}
```

You can test the function with the provided test cases:

```go
fmt.Println(MaxElement([]int{1, 2, 3}))  // Output: 3
fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))  // Output: 123
```

This implementation uses a `for` loop to iterate through the list and a range clause to access each element. The `max` variable is updated only if a larger element is found. Finally, the maximum element is returned as the result.

Note that this implementation assumes that the input list `l` is not empty. If you need to handle the case where the list can be empty, you can add a check at the beginning of the function to return an error or a default value in such cases.

Additionally, it's worth mentioning that Go provides built-in functions like `math.Max` and `math.MaxInt` that can be used to find the maximum value of a slice or an integer respectively. These functions are optimized and can be more efficient than a custom implementation, especially for larger lists.

Here's an example of using `math.Max` to find the maximum element in a list:

