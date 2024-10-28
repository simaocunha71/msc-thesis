Here is a solution that uses a loop to iterate over the first k elements of the array and checks if each element has at most two digits. If it does, it adds the element to the sum.

```go
import (
    "strconv"
)

func AddElements(arr []int, k int) int {
    var sum int
    for i := 0; i < k; i++ {
        str := strconv.Itoa(arr[i])
        if len(str) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}
```

This solution has a time complexity of O(k), where k is the number of elements in the array. This is because it needs to iterate over the first k elements of the array. The space complexity is O(1), which means the space required does not change with the size of the input array. This is because it only uses a fixed amount of space to store the sum and the loop variable.