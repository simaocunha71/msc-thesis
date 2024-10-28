```go
package main

import (
    "fmt"
    "math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {
    var largestNegative int = math.MinInt32
    var smallestPositive int = math.MaxInt32
    var foundNegative, foundPositive bool

    for _, v := range lst {
        if v < 0 {
            if v > largestNegative {
                largestNegative = v
            }
            foundNegative = true
        } else if v > 0 {
            if v < smallestPositive {
                smallestPositive = v
            }
            foundPositive = true
        }
    }

    if !foundNegative {
        largestNegative = nil
    }
    if !foundPositive {
        smallestPositive = nil
    }

    return [2]interface{}{largestNegative, smallestPositive}
}

func main() {
    fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))  // (nil, 1)
    fmt.Println(LargestSmallestIntegers([]int{}))                // (nil, nil)
    fmt.Println(LargestSmallestIntegers([]int{0}))               // (nil, nil)
}
```

This program defines a function `LargestSmallestIntegers` that takes a slice of integers as input. It initializes two variables `largestNegative` and `smallestPositive` to the minimum and maximum possible integer values respectively. It also initializes two boolean variables `foundNegative` and `foundPositive` to `false`.

It then iterates over the input slice, updating `largestNegative` and `smallestPositive` if it finds a negative or positive integer respectively. If it finds a negative integer, it checks if it is larger than the current `largestNegative` and updates it if necessary. If it finds a positive integer, it checks if it is smaller than the current `smallestPositive` and updates it if necessary.

After iterating over the slice, it checks if it found any negative or positive integers. If not, it sets `largestNegative` and `smallestPositive` to `nil` respectively.

Finally, it returns a tuple containing `largestNegative` and `smallestPositive` as interfaces. In Go, interfaces can be used to represent values of different types, so `nil` is a valid value for an interface.

The `main` function tests the `LargestSmallestIntegers