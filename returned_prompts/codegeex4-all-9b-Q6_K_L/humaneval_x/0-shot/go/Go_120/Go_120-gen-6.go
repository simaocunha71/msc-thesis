You can use the sort.Slice() function from the sort package to sort the array in descending order and then return the first k elements. Here is the code:

```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}
```

This code will sort the array in descending order and then return the first k elements.