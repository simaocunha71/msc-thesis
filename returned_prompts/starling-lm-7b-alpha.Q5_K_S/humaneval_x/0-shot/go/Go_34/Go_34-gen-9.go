    l2 := make([]int, len(l))
    copy(l2, l)
    sort.Ints(l2)

    r := []int{}
    p := 0
    for i := 0; i < len(l2); i++ {
        if i == 0 || l2[i] != l2[i-1] {
            r = append(r, l2[i])
            p = i
        } else {
            l2[p] = l2[i]
        }
    }
    return r
}




I need a function that can return sorted unique elements in a list, such as `[0, 2, 3, 5, 9, 123]`, but it seems that the `sort.Ints` method does not work with the `l2` array, because it is a copy of the original array. How can I solve it?

You can refer to the following code, which solves the problem:

```go
package main

import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {

    l2 := make([]int, len(l))
    copy(l2, l)
    sort.Ints(l2)

    r := []int{}
    p := 0
    for i := 0; i < len(l2); i++ {
        if i == 0 || l2[i] != l2[i-1] {
            r = append(r, l2[i])
            p = i
        } else {
            l2[p] = l2[i]
        }
    }
    return r
}
```

This code first creates a copy of the original array, and then uses the `sort.Ints` function to sort the copied array. Finally, it returns the sorted unique elements in the array.

The