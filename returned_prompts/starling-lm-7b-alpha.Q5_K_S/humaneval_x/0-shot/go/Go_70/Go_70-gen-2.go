    for i := 0; i < len(lst); i++ {
        fmt.Println(lst[i])
    }
    return lst
}

// StrangeSortList([]) == []
func StrangeSortList(lst []int) []int {
    sort.Slice(lst[:], func(i, j int) bool {
        return lst[i] < lst[j]
    })
    return lst
}

In Go, the `sort` package provides several sorting functions. For example, the `sort.Slice` function can be used to sort a slice in place. Here is an example of how to use `sort.Slice` to sort a slice of integers from smallest to largest:
```go
package main

import "fmt"
import "sort"

func main() {
    lst := []int{5, 5, 5, 5}
    fmt.Println("Before:", lst)
    sort.Slice(lst[:], func(i, j int) bool {
        return lst[i] < lst[j]
    })
    fmt.Println("After:", lst)
}
```
In this example, we define a slice of integers `lst` and print it out before sorting. We then use `sort.Slice` to sort the slice in place. The `sort.Slice` function takes two arguments: the slice to be sorted and a function that defines the sorting order. In this case, we pass a function that returns true if the element at index `i` should come before the element at index `j` in the sorted list. Finally, we print out the sorted slice.

The `sort.Slice` function is useful when you want to sort a slice based on a custom sorting order. In this case, the `sort.Slice` function is used to sort the slice in ascending order, but you can pass a different function to define a different sorting order.

Note that the `sort.Slice` function sorts the slice in place, meaning that the original slice is modified. If you want to keep the original slice intact, you can make a copy of it before sorting.

Overall, the `sort` package in Go provides a convenient way to sort slices in various ways,