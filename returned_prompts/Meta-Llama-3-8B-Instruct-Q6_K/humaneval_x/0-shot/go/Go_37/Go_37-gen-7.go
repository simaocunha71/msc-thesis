Here is a possible solution:
```go
func SortEven(l []int) []int {
    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i%2 == 0 {
            // even index, sort the value
            sort.Ints([]int{l[i]})
            result[i] = l[i]
        } else {
            // odd index, keep the value the same
            result[i] = l[i]
        }
    }
    return result
}
```
This function creates a new slice `result` with the same length as the input slice `l`. It then iterates over the indices of `l`, and for each index `i`:

* If `i` is even, it sorts the value at that index using `sort.Ints`, and assigns the sorted value to the corresponding index in `result`.
* If `i` is odd, it simply assigns the value at that index in `l` to the corresponding index in `result`.

Finally, the function returns the `result` slice.

Note that this function uses the `sort.Ints` function from the Go standard library to sort the values at even indices. This function sorts the values in-place, so it does not create a new slice, but rather modifies the original slice. This is why we need to create a new slice `result` to store the sorted values.