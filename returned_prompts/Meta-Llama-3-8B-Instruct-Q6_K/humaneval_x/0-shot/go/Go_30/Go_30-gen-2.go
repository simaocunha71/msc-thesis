```go
func GetPositive(l []int) []int {
    var result []int
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}
```


The problem is asking to create a function called `GetPositive` that takes a list of integers as input and returns a new list containing only the positive numbers from the original list.

Here's a simple solution in Go:

```go
func GetPositive(l []int) []int {
    var result []int
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}
```

This function uses a for loop to iterate over the input list `l`. For each number `v` in the list, it checks if the number is positive (i.e., `v > 0`). If it is, it appends the number to the `result` slice. Finally, the function returns the `result` slice, which contains only the positive numbers from the original list.

For example, if you call `GetPositive([-1, 2, -4, 5, 6])`, the function will return `[2, 5, 6]`. If you call `GetPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])`, the function will return `[5, 3, 2, 3, 9, 123, 1]`.