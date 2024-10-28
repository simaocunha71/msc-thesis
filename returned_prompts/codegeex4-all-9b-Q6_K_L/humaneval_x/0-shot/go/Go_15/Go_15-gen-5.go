```go
func StringSequence(n int) string {
    var nums []string
    for i := 0; i <= n; i++ {
        nums = append(nums, strconv.Itoa(i))
    }
    return strings.Join(nums, " ")
}
```