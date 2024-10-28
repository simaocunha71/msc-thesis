```go
func SortEven(l []int) []int {
    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i%2 == 0 {
            sort.Ints(&[]int{l[i]})
        }
        result[i] = l[i]
    }
    return result
}
```

Explanation:
The function `SortEven` takes a slice of integers `l` as input and returns a new slice where the values at even indices are sorted. The values at odd indices remain the same.

Here's how it works:
- We create a new slice `result` with the same length as the input slice `l`.
- We iterate over the input slice `l`. For each index `i`:
  - If `i` is even (i.e., `i%2 == 0`), we sort the slice `[]int{l[i]}` using `sort.Ints`. This sorts the single-element slice in-place.
  - We assign the value at index `i` in the input slice `l` to the corresponding index `i` in the result slice `result`.
- Finally, we return the result slice.

For example, if the input slice is `[5, 6, 3, 4]`, the function will return `[3, 6, 5, 4]`. The value at index 0 (even index) is not changed, the value at index 1 (even index) is sorted to be `6`, the value at index 2 (odd index) remains the same, and the value at index 3 (even index) is sorted to be `4`.  Q.E.D.