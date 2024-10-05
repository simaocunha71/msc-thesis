    if len(array) == 0{
        return []int{}
    }

    if len(array) == 1{
        return []int{array[0]}
    }

    sum := array[0] + array[len(array)-1]
    sortedArray := make([]int, len(array))
    copy(sortedArray, array)

    if sum % 2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(sortedArray)))
    } else {
        sort.Ints(sortedArray)
    }

    return sortedArray
}

// How to run the code:
// * Write your code to a new file, say `main.go`
// * Run the file with the following command: `go run main.go`
// * You should get the output as expected.

```

## 代码解释

这段代码首先检查数组的长度。如果长度为0，它将返回一个空数组。如果长度为1，它将返回一个只包含一个元素的数组。

然后，它计算数组的第一个和最后一个元素的和。如果和是偶数，它将通过将排序后的数组反转来返回一个降序排列的数组。如果和是奇数，它将通过将排序后的数组升序排列来返回一个升序排列的数组。

最后，它返回排序后的数组。

## 测试

你可以使用以下测试用例来测试这段代码：

```go
func main() {
    fmt.Println(SortArray([]int{})) // 期望输出: []
    fmt.Println(SortArray([]int{5})) // 期望输出: [5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5})) // 期望输出: [0, 1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5, 6})) //