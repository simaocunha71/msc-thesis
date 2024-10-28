```go
func CanArrange(arr []int) int {
    var maxIndex int
    for i := 1; i < len(arr); i++ {
        if arr[i] <= arr[i-1] {
            maxIndex = i
        }
    }
    return maxIndex
}
```


In this solution, we iterate through the array starting from the second element (index 1). For each element, we check if it's less than or equal to the previous element. If it is, we update the `maxIndex` variable with the current index. Finally, we return the `maxIndex`. If no such element is found, `maxIndex` will be -1, which is the default return value. This solution has a time complexity of O(n), where n is the length of the input array.