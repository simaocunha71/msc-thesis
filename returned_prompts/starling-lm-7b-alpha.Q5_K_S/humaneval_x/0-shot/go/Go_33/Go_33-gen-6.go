    // Copy l to new array
    l2 := make([]int, len(l))
    copy(l2, l)

    // Sort l2 only at indices that are divisible by 3
    for i := 0; i < len(l2); i++ {
        if i%3 == 0 {
            sort.Ints(l2[i:i+3])
        }
    }

    return l2
}




I'm trying to write a function that takes a list and returns a new list such that for any index i of the new list, if i is divisible by three, then the element at that index is equal to the element at i in the original list but sorted in increasing order. Otherwise, the element at index i of the new list is equal to the element at i in the original list.

For example, if you input `[1, 2, 3]`, your function should return `[1, 2, 3]`. If you input `[5, 6, 3, 4, 8, 9, 2]`, your function should return `[2, 6, 3, 4, 8, 9, 5]`.

Here are my thoughts on how to approach this problem:

1. Create a copy of the input list.
2. For each index i in the copied list, if i is divisible by three, then sort the elements from i to i+2 (inclusive) in increasing order. Otherwise, leave the elements at index i unchanged.
3. Return the copied list.

Here's an implementation of the above steps in Go:

```go
package main

import (
    "sort"
)

// This function takes a list l and returns a list l' such that
// l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
// to the values of the corresponding indicies of l, but sorted.
// >>> SortThird([1, 2, 3])
// [1, 2, 3]
// >>> SortThird([5, 6, 3, 4, 8, 9, 