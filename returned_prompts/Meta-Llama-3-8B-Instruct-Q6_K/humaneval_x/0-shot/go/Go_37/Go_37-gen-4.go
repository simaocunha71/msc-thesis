Here is the implementation of the function:
```go
func SortEven(l []int) []int {
    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i%2 == 0 {
            sort.Ints(l[i/2:i/2+1])
            result[i] = l[i]
        } else {
            result[i] = l[i]
        }
    }
    return result
}
```
Here's how it works:

1. Create a new slice `result` with the same length as `l`.
2. Iterate over `l` with an index `i`.
3. If `i` is even, sort the slice of `l` from `i/2` to `i/2+1` (inclusive) and assign the sorted slice to `result[i]`. Otherwise, just assign `l[i]` to `result[i]`.
4. Return the `result` slice.

Note that the `sort.Ints` function is used to sort the slice of `l` from `i/2` to `i/2+1`. This function sorts the slice in place, so we don't need to create a new slice to store the sorted values. Also, the `i/2` expression is used to calculate the starting index of the slice to be sorted, and `i/2+1` is used to calculate the ending index. The `+1` is needed because the slice indices in Go are 0-based.