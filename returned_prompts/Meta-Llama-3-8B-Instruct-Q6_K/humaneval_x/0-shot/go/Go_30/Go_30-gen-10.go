```go
func GetPositive(l []int) []int {
    result := make([]int, 0, len(l))
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}
```

Explanation:

*   We create a new slice `result` with a capacity equal to the length of the input slice `l`. This is done using the `make` function with a capacity argument.
*   We iterate over the input slice `l` using a range loop.
*   For each element `v` in the input slice, we check if it is greater than 0 using the `if` statement.
*   If `v` is positive, we append it to the `result` slice using the `append` function.
*   Finally, we return the `result` slice, which now contains only the positive numbers from the original input slice.