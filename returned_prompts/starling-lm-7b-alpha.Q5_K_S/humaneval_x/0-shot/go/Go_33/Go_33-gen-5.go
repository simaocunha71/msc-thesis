    l2 := make([]int, len(l))

    for i := 0; i < len(l); i++ {
        if i%3 == 0 {
            l2[i] = sort.IntSlice(l[i:i+3]).Slice()
        } else {
            l2[i] = l[i]
        }
    }

    return l2
}




I have a function that takes a list and returns a list where the values at the indices that are divisible by three are sorted, while the other values remain the same. However, I am having an error in the function. The error is that "sort.IntSlice(l[i:i+3]) is not exported". I think it's because I am using sort.IntSlice in a wrong place. But I don't know how to use it correctly.

Here is the code:

package main

import (
    "fmt"
    "sort"
)

func main() {
    fmt.Println(SortThird([]int{1, 2, 3}))
    fmt.Println(SortThird([]int{5, 6, 3, 4, 8, 9, 2}))
}

func SortThird(l []int) []int {
    l2 := make([]int, len(l))

    for i := 0; i < len(l); i++ {
        if i%3 == 0 {
            l2[i] = sort.IntSlice(l[i:i+3]).Slice()
        } else {
            l2[i] = l[i]
        }
    }

    return l2
}

The error is "sort.IntSlice(l[i:i+3]) is not exported".

I am using sort.IntSlice to sort a slice of integers. However, the error message says that sort.IntSlice(l[i:i+3]) is not exported. This is because the sort package is not part of the standard Go library.

To use sort.IntSlice, you need to import the "sort" package. Here's how you can do it:

```go
package