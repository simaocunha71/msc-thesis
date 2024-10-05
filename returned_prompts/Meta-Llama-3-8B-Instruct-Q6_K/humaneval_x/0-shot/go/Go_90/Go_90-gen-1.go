Here is a simple Go function that implements the `NextSmallest` function:

```go
package main

import (
    "math"
    "sort"
)

// You are given a list of integers.
// Write a function NextSmallest() that returns the 2nd smallest element of the list.
// Return nil if there is no such element.
// 
// NextSmallest([1, 2, 3, 4, 5]) == 2
// NextSmallest([5, 1, 4, 3, 2]) == 2
// NextSmallest([]) == nil
// NextSmallest([1, 1]) == nil
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    if len(lst) == 2 {
        return nil
    }
    return lst[1]
}

func main() {
    result := NextSmallest([]int{1, 2, 3, 4, 5})
    if result != nil {
        println(result) // prints 2
    } else {
        println("nil")
    }
}
```

This function first checks if the list has less than 2 elements. If so, it returns `nil`. Then it sorts the list. If the list has only 2 elements after sorting, it returns `nil`. Otherwise, it returns the second smallest element, which is at index 1 in the sorted list. The `main` function demonstrates how to use this function. It prints `2` for the input `[1, 2, 3, 4, 5]`. If the input is an empty list, it prints `nil`. If the input is a list with only one element, it also prints `nil`. 