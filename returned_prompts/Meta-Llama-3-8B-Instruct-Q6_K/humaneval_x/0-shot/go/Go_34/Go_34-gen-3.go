Here is a simple solution using a set and the built-in `sort` function in Go:

```go
package main

import (
    "fmt"
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    set := make(map[int]bool)
    for _, v := range l {
        set[v] = true
    }
    keys := make([]int, 0, len(set))
    for k := range set {
        keys = append(keys, k)
    }
    sort.Ints(keys)
    return keys
}

func main() {
    l := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
    result := Unique(l)
    fmt.Println(result)
}
```

This program creates a map from the input list, then converts the map's keys to a slice and sorts it. The result is a slice of unique elements in sorted order. 

When you run this program, it will print: `[0 2 3 5 9 123]` which are the unique elements from the input list in sorted order. 

Note: The `sort` function is used to sort the slice of unique elements. This function sorts the slice in ascending order by default. If you want to sort the slice in descending order, you can use the `sort.Ints(keys)` function with a custom sorting function. 

Also, the `sort` function is stable, which means that when multiple records have the same key, their original order is preserved. This is important if you want to maintain the order of equal elements.  If you want to sort the slice in descending order and also want to maintain the order of equal elements, you can use the `sort.Stable` function.  However, the `sort.Stable` function is not available in Go's standard library. You can use the `sort.Ints` function with a custom sorting function to achieve this.  For example:

```go
sort.Sort(sort.IntSlice(keys).Reverse())
```

This will sort the slice in descending order and also maintain the order of equal elements.  However, this is not necessary in this specific problem because the problem statement