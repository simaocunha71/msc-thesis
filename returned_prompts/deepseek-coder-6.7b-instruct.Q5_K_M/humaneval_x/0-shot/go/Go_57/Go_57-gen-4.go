
    if len(l) == 0 || len(l) == 1 {
        return true
    }

B:

    var inc, dec bool

C:

    for i := 0; i < len(l)-1; i++ {

D:

        if l[i] < l[i+1] {
            if dec == true {
                return false
            }
            inc = true
        } else if l[i] > l[i+1] {
            if inc == true {
                return false
            }
            dec = true
        }
    }

E:

    return true
}
```

## Test

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(Monotonic([]int{1, 2, 4, 20}))  // true
    fmt.Println(Monotonic([]int{1, 20, 4, 10}))  // false
    fmt.Println(Monotonic([]int{4, 1, 0, -10}))  // true
}
```

## Explanation

The function `Monotonic` checks whether the given list is monotonically increasing or decreasing.

The steps to solve this problem are as follows:

1. Handle the edge cases where the list is empty or has only one element. In such cases, return `true` because a list with a single element or no elements is considered monotonically increasing or decreasing.

2. Initialize two variables `inc` and `dec` to `false`. These will be used to keep track of whether the list is monotonically increasing or decreasing.

3. Loop through the list, comparing each element with the next one. If the current element is less than the next one, set `inc` to `true`. If the current element is greater than the next one, set `dec` to `true`. If at any point, both `inc` and `dec` are `true`, return `false` because a list cannot be both monotonically increasing and decreasing.

4. If the loop completes without returning `false`, return `true` because