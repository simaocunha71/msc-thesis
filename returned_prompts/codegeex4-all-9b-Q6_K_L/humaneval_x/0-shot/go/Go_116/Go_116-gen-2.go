```go
func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        x, y := arr[i], arr[j]
        if bits.OnesCount(uint(x)) == bits.OnesCount(uint(y)) {
            return x < y
        }
        return bits.OnesCount(uint(x)) < bits.OnesCount(uint(y))
    })
    return arr
}
```
解释：
1. `sort.Slice` 函数用于对切片进行排序。
2. `func(i, j int) bool` 是一个比较函数，用于比较两个元素的大小。
3. `x, y := arr[i], arr[j]` 获取要比较的两个元素。
4. `bits.OnesCount(uint(x))` 返回 x 的二进制表示中 1 的个数。
5. `if bits.OnesCount(uint(x)) == bits.OnesCount(uint(y))` 判断 x 和 y 的 1 的个数是否相等。
6. `return x < y` 如果 x 和 y 的 1 的个数相等，则按照它们的十进制值进行比较。
7. `return bits.OnesCount(uint(x)) < bits.OnesCount(uint(y))` 如果 x 和 y 的 1 的个数不相等，则按照它们的 1 的个数进行比较。