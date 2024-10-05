```
func GetPositive(l []int) []int {
    result := make([]int, 0)
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}
```



Solution:

The problem asks to write a function that takes a list of integers as input and returns a new list containing only the positive numbers from the input list.

Here is a simple and efficient solution in Go:

```go
func GetPositive(l []int) []int {
    result := make([]int, 0)
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}
```

This function uses a slice `result` to store the positive numbers. It then iterates over the input list `l` using a range loop. For each number `v` in the input list, it checks if `v` is greater than 0. If it is, it appends `v` to the `result` slice. Finally, it returns the `result` slice.

This function has a time complexity of O(n), where n is the length of the input list, because it needs to iterate over the entire list to find the positive numbers. It has a space complexity of O(m), where m is the number of positive numbers in the input list, because it needs to store these numbers in the `result` slice.