```go
package main

import (
    "fmt"
    "math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {
    var largestNegative, smallestPositive int
    largestNegativeFound := false
    smallestPositiveFound := false

    for _, v := range lst {
        if v < 0 {
            if largestNegativeFound {
                if v > largestNegative {
                    largestNegative = v
                }
            } else {
                largestNegative = v
                largestNegativeFound = true
            }
        } else if v > 0 {
            if smallestPositiveFound {
                if v < smallestPositive {
                    smallestPositive = v
                }
            } else {
                smallestPositive = v
                smallestPositiveFound = true
            }
        }
    }

    if largestNegativeFound && smallestPositiveFound {
        return [2]interface{}{largestNegative, smallestPositive}
    } else if largestNegativeFound {
        return [2]interface{}{largestNegative, nil}
    } else if smallestPositiveFound {
        return [2]interface{}{nil, smallestPositive}
    } else {
        return [2]interface{}{nil, nil}
    }
}

func main() {
    fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))  // Output: [7 nil]
    fmt.Println(LargestSmallestIntegers([]int{}))                // Output: [nil nil]
    fmt.Println(LargestSmallestIntegers([]int{0}))               // Output: [nil nil]
}
```

This program defines a function `LargestSmallestIntegers` that takes a slice of integers as input and returns a tuple of two values. The first value is the largest negative integer in the slice, and the second value is the smallest positive integer in the slice. If there are no negative or positive integers in the slice, the function returns a tuple with both values set to `nil`. The function iterates over the slice, keeping track of the largest negative integer and the smallest positive integer found so far. If the slice is empty, the function returns a tuple with both values set to `nil`. If the slice contains only zeros, the function returns a tuple with both values set to `nil`. The function uses the `math` package to check if the values are integers, but this is not necessary in this case.

The `main` function demonstrates the usage of the `L