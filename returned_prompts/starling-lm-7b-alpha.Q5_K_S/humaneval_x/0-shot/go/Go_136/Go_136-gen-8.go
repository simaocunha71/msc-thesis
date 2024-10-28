
Here is a solution in Go:

```go
package main

import "fmt"

func LargestSmallestIntegers(lst []int) [2]interface{}{
    var a, b int
    var ap, bp bool
    for _, v := range lst {
        if v < 0 {
            if a == 0 {
                a = v
            } else if v < a {
                a = v
            }
            ap = true
        }
        if v > 0 {
            if b == 0 {
                b = v
            } else if v < b {
                b = v
            }
            bp = true
        }
    }
    if ap == true && bp == true {
        return [2]interface{}{a, b}
    } else {
        return [2]interface{}{nil, nil}
    }
}

func main() {
    fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // (nil, 1)
    fmt.Println(LargestSmallestIntegers([]int{}))                // (nil, nil)
    fmt.Println(LargestSmallestIntegers([]int{0}))               // (nil, nil)
}
```

Explanation:

The function `LargestSmallestIntegers` takes a slice of integers as input and returns a tuple of two integers.

The function initializes two variables `a` and `b` to store the largest negative integer and the smallest positive integer, respectively. It also initializes two boolean variables `ap` and `bp` to track whether `a` and `b` have been assigned a value.

The function then iterates over each element in the input slice using a `for ... range` loop. For each element, it checks if it is negative or positive. If it is negative, it updates `a` if `a` is not already assigned or if the current element is larger than the current value of `a`. It also sets `ap` to true to indicate that `a` has a value. Similarly, if the element is positive,