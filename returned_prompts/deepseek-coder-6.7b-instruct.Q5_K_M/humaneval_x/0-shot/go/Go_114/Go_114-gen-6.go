    return minSubArray(nums)
}

func minSubArray(nums []int) int {
    total := 0
    min := math.MaxInt64
    for _, num := range nums {
        total += num
        if total < min {
            min = total
        }
        total = int(math.Min(float64(total), float64(num)))
    }
    return min
}
```

## Solution

```go
package main

import (
    "fmt"
    "math"
)

func Minsubarraysum(nums []int) int {
    return minSubArray(nums)
}

func minSubArray(nums []int) int {
    total := 0
    min := 0
    for _, num := range nums {
        total += num
        min = int(math.Min(float64(min), float64(total)))
        if total > 0 {
            total = 0
        }
    }
    return -min
}

func main() {
    fmt.Println(Minsubarraysum([]int{2, -3, 4, -1, 2, 4})) // Output: 1
    fmt.Println(Minsubarraysum([]int{-1, -2, -3})) // Output: -6
}
```

## Test case

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(Minsubarraysum([]int{2, 3, 4, 1, 2, 4})) // Expected output: 1
    fmt.Println(Minsubarraysum([]int{-1, -2, -3})) // Expected output: -6
    fmt.Println(Minsubarraysum([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4})) // Expected output: -3
    fmt.Println(Minsubarraysum([]int{-2, -3, 4, -1