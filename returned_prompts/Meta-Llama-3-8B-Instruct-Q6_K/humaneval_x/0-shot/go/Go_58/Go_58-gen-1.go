Here is a possible implementation of the `Common` function in Go:
```go
func Common(l1 []int, l2 []int) []int {
    // Create a set of unique elements from l1
    set1 := make(map[int]bool)
    for _, v := range l1 {
        set1[v] = true
    }

    // Create a set of unique elements from l2
    set2 := make(map[int]bool)
    for _, v := range l2 {
        set2[v] = true
    }

    // Find the intersection of the two sets
    common := make([]int, 0)
    for k := range set1 {
        if set2[k] {
            common = append(common, k)
        }
    }

    // Sort the common elements
    sort.Ints(common)

    return common
}
```
This implementation uses two `map`s to create sets of unique elements from each input list, and then finds the intersection of the two sets by iterating over the keys of the first set and checking if each key is also present in the second set. The resulting common elements are stored in a slice and returned.

You can test this function using the examples you provided:
```go
func main() {
    l1 := []int{1, 4, 3, 34, 653, 2, 5}
    l2 := []int{5, 7, 1, 5, 9, 653, 121}
    common := Common(l1, l2)
    fmt.Println(common) // Output: [1 5 653]

    l1 = []int{5, 3, 2, 8}
    l2 = []int{3, 2}
    common = Common(l1, l2)
    fmt.Println(common) // Output: [2 3]
}
```
Note that this implementation assumes that the input lists do not contain duplicate elements. If the input lists may contain duplicates, you may need to modify the implementation to handle this case. For example, you could use a `set` data structure that allows duplicates, or you could use a different approach to find the common elements.