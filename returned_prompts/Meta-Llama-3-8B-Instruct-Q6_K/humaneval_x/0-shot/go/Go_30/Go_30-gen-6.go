You can solve this problem by using Go language. Here is the solution:

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

In this solution, we create an empty slice `result` to store the positive numbers. Then we iterate over the input slice `l` using a for loop. For each number `v` in the slice, we check if it's positive (i.e., `v > 0`). If it is, we append it to the `result` slice. Finally, we return the `result` slice. This solution has a time complexity of O(n), where n is the length of the input slice, because we iterate over the slice once. The space complexity is O(n) as well, because in the worst case, the `result` slice can have the same length as the input slice.