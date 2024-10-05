Here is a simple implementation using a set to remove duplicates and the sort package to sort the elements:

```go
import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    m := make(map[int]bool)
    for _, v := range l {
        m[v] = true
    }
    var result []int
    for k := range m {
        result = append(result, k)
    }
    sort.Ints(result)
    return result
}
```

This function creates a map from the input list, which automatically removes duplicates because a map can't have duplicate keys. It then creates a new slice from the map keys and sorts it using the `sort.Ints` function from the `sort` package. 

This function has a time complexity of O(n log n) due to the sorting, where n is the number of unique elements in the input list. The space complexity is O(n) for the map and the result slice. 

Note that this function does not preserve the original order of elements. If you need to preserve the original order, you can use a different approach, such as using a slice of slices to group elements by their values, and then concatenating the slices in the original order. However, this approach would be more complex and less efficient. 

Also, note that this function assumes that the input list does not contain duplicate elements with different types. If the input list can contain elements with different types, you would need a more complex approach to handle this. 

You can test this function using the following code:

```go
func main() {
    l := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
    result := Unique(l)
    fmt.Println(result)
}
```

This code will print `[0 2 3 5 9 123]`, which are the unique elements in the input list, sorted in ascending order. 