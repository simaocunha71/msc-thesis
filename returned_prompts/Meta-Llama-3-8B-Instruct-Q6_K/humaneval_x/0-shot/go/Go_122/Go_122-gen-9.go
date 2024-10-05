Here is the solution in Go:

```go
import (
    "strconv"
)

func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k && i < len(arr); i++ {
        str := strconv.Itoa(arr[i])
        if len(str) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}
```

This function iterates over the first `k` elements of the array. For each element, it converts it to a string and checks the length of the string. If the length is less than or equal to 2, it means the number has at most two digits, so it adds the number to the sum. Finally, it returns the sum.