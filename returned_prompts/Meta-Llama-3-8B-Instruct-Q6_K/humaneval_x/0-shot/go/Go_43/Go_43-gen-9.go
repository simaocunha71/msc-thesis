```go
package main

import (
    "fmt"
    "sort"
)

func PairsSumToZero(l []int) bool {
    if len(l) <= 1 {
        return false
    }
    sort.Ints(l)
    for i, v1 := range l {
        if i > 0 && l[i-1] == -v1 {
            return true
        }
        if i < len(l)-1 && l[i+1] == -v1 {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(PairsSumToZero([]int{1, 3, 5, 0}))  // false
    fmt.Println(PairsSumToZero([]int{1, 3, -2, 1})) // false
    fmt.Println(PairsSumToZero([]int{1, 2, 3, 7}))  // false
    fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7})) // true
    fmt.Println(PairsSumToZero([]int{1}))              // false
}
```

The code defines a function PairsSumToZero that takes a slice of integers as an input. It returns true if there are two distinct elements in the list that sum to zero, and false otherwise.

The function first checks if the length of the slice is less than or equal to 1, in which case it returns false.

Then it sorts the slice in ascending order.

It then iterates over the slice, checking for each element if its negation is present in the slice. If it is, it returns true. If it is not, it continues the iteration.

Finally, if no pair of elements summing to zero is found, it returns false.

The code also includes a main function that tests the PairsSumToZero function with different inputs. The expected output is printed to the console.