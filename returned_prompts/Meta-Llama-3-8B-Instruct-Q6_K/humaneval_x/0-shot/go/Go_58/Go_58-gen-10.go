Here is a solution for the problem using Go language. This solution uses the built-in `sort` package to sort the lists and the `set` package to find the common elements.

```go
package main

import (
    "fmt"
    "sort"
)

func Common(l1 []int, l2 []int) []int {
    // convert the slices to sets
    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    for _, val := range l1 {
        set1[val] = true
    }
    for _, val := range l2 {
        set2[val] = true
    }

    // find the intersection of the sets
    var common []int
    for k := range set1 {
        if set2[k] {
            common = append(common, k)
        }
    }

    // sort the common elements
    sort.Ints(common)

    return common
}

func main() {
    fmt.Println(Common([]int{1, 4, 3, 34, 653, 2, 5}, []int{5, 7, 1, 5, 9, 653, 121}))
    fmt.Println(Common([]int{5, 3, 2, 8}, []int{3, 2}))
}
```

This program will output:

```
[1 5 653]
[2 3]
```

This is the expected output for the given test cases. The `Common` function takes two slices of integers as input, converts them to sets using a map, finds the intersection of the sets (i.e., the common elements), and returns the common elements in sorted order. The `main` function tests the `Common` function with the given test cases.