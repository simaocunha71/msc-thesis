    maxs := make([]int, len(numbers))
    currentMax := math.MinInt64

    for i, num := range numbers {
        if num > currentMax {
            currentMax = num
        }
        maxs[i] = currentMax
    }

    return maxs
}
```

The function `RollingMax` creates an empty slice of the same length as the input slice. For each number in the input slice, it checks if the number is greater than the current maximum number found. If it is, the current maximum is updated. The new maximum is then stored in the corresponding position in the `maxs` slice. The function finally returns the `maxs` slice.

Here, the time complexity of the function is O(n), where n is the length of the input slice, because it needs to iterate through the input slice once. The space complexity is also O(n), because it creates a new slice of the same length as the input slice.

Note: The `math.MinInt64` is used as the initial maximum value to ensure that any integer from the input list is greater than it.

This function can be used in various applications such as finding the maximum value in a window of size k in a data stream, or finding the maximum value in a subarray of a given array.

You can use this function in Go as follows:

```go
package main

import (
    "fmt"
)

func main() {
    numbers := []int{1, 2, 3, 2, 3, 4, 2}
    fmt.Println(RollingMax(numbers))
    // Output: [1 2 3 3 3 4 4]
}
```

In this code, the `RollingMax` function is called with a slice of integers as an argument, and the result is printed.
*/
package main

import (
	"fmt"
)

func main() {
	numbers := []int{1, 2, 3, 2, 3, 4, 2}
	fmt.Println(RollingMax(numbers))
	// Output: [1 2 3 3