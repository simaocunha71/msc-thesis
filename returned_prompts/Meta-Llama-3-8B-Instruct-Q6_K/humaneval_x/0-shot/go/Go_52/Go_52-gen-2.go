```go
package main

import (
    "fmt"
)

func BelowThreshold(l []int, t int) bool {
    for _, v := range l {
        if v >= t {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100))  // true
    fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))   // false
}
```



Output:

```
true
false
```



Explanation:

This function `BelowThreshold` takes a slice of integers `l` and an integer `t` as input. It iterates over each number `v` in the slice using a `for` loop with a range. For each number, it checks if the number is greater than or equal to the threshold `t`. If it finds a number that is greater than or equal to the threshold, it immediately returns `false`. If it iterates over the entire slice without finding such a number, it returns `true`.

In the `main` function, we call `BelowThreshold` with two different sets of input and print the output. The first call checks if all numbers in the slice `[1, 2, 4, 10]` are below the threshold `100`, which they are, so the output is `true`. The second call checks if all numbers in the slice `[1, 20, 4, 10]` are below the threshold `5`, which they are not, so the output is `false`.