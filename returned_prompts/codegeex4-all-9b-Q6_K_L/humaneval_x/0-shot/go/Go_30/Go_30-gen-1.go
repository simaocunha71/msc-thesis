Here is the solution in Go:

```go
func GetPositive(l []int) []int {
    var positiveNumbers []int
    for _, value := range l {
        if value > 0 {
            positiveNumbers = append(positiveNumbers, value)
        }
    }
    return positiveNumbers
}
```

This function iterates over each value in the input list `l`, and if the value is greater than 0, it appends it to the `positiveNumbers` slice. Finally, it returns the `positiveNumbers` slice.