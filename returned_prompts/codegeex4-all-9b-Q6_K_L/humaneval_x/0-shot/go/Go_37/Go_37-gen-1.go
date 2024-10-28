Here is the Go code that solves the problem:

```go
func SortEven(l []int) []int {
    // Get the values at the even indices
    evenValues := make([]int, 0)
    for i := 0; i < len(l); i += 2 {
        evenValues = append(evenValues, l[i])
    }

    // Sort the even values
    sort.Ints(evenValues)

    // Reconstruct the original list with the sorted even values
    for i := 0; i < len(l); i += 2 {
        l[i] = evenValues[i/2]
    }

    return l
}
```

This function first extracts the values at the even indices of the input list `l` into a separate slice `evenValues`. It then sorts `evenValues` in ascending order using the `sort.Ints` function. Finally, it reconstructs the original list `l` by replacing the values at the even indices with the sorted values from `evenValues`.