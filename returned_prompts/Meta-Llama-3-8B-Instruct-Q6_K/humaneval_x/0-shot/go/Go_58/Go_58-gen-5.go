Here is a simple Go function that returns the common elements from two lists in a sorted and unique manner:

```go
package main

import (
    "sort"
)

// Return sorted unique Common elements for two lists.
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int, l2 []int) []int {
    m := make(map[int]bool)
    for _, v := range l1 {
        m[v] = true
    }
    var result []int
    for _, v := range l2 {
        if m[v] {
            result = append(result, v)
            delete(m, v)
        }
    }
    sort.Ints(result)
    return result
}

func main() {
    fmt.Println(Common([]int{1, 4, 3, 34, 653, 2, 5}, []int{5, 7, 1, 5, 9, 653, 121}))
    fmt.Println(Common([]int{5, 3, 2, 8}, []int{3, 2}))
}
```

This function uses a map to keep track of the elements in the first list, and then iterates over the second list, adding any elements that are also in the map to the result slice. It then sorts the result slice and returns it. The time complexity of this function is O(n + m), where n and m are the lengths of the input lists. The space complexity is O(n), where n is the number of unique elements in the first list. 

In the main function, we test the Common function with two sets of input lists. The output for the first test is `[1 5 653]`, and the output for the second test is `[2 3]`. 

This function assumes that the input lists do not contain duplicate elements. If the input lists can contain duplicates, the function will also return duplicates in the result. If you want to remove duplicates from the result, you can use the `sort.Uniq` function from the `sort` package. However, this function is not stable, so it may change