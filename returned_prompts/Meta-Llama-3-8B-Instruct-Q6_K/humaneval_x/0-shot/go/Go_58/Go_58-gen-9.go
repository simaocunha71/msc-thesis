Here is a simple solution that uses a set to keep track of unique elements and then sorts the common elements:

```go
import (
    "sort"
)

func Common(l1 []int, l2 []int) []int {
    set := make(map[int]bool)
    for _, v := range l1 {
        set[v] = true
    }
    var common []int
    for _, v := range l2 {
        if set[v] {
            common = append(common, v)
            set[v] = false
        }
    }
    sort.Ints(common)
    return common
}
```

This function first creates a set from the elements of `l1`. Then it iterates over the elements of `l2` and checks if each element is in the set. If it is, the element is added to the `common` slice and removed from the set to avoid duplicates. Finally, the function sorts the `common` slice and returns it. 

This solution has a time complexity of O(n) where n is the length of `l2`, because it iterates over `l2` once. The space complexity is also O(n) because in the worst case, all elements of `l2` are common with `l1`. 

Note: The order of the elements in the output slice is not guaranteed to be the same as the order they appear in the input slices, because the `sort.Ints` function sorts the slice in ascending order. If you need to preserve the order of the elements, you can use a different sorting algorithm or a different data structure. 