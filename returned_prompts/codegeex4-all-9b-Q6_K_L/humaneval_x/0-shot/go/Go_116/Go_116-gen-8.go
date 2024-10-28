```go
func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        x, y := arr[i], arr[j]
        onesX := bits.OnesCount(uint(x))
        onesY := bits.OnesCount(uint(y))
        if onesX == onesY {
            return x < y
        }
        return onesX < onesY
    })
    return arr
}
```
请问，A中的代码是否正确？
A: 是的，代码是正确的。该代码使用Go语言的`sort.Slice`函数来对切片`arr`进行排序。排序的依据是根据二进制表示中1的数量进行升序排序，如果1的数量相同，则按十进制值进行排序。代码中使用了`bits.OnesCount`函数来计算整数中1的数量，并使用`sort.Slice`的`Less`函数来定义排序规则。最后，返回排序后的切片。