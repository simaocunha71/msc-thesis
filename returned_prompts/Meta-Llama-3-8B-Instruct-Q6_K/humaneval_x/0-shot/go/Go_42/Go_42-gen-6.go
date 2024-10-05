```
func IncrList(l []int) []int {
    result := make([]int, len(l))
    for i, v := range l {
        result[i] = v + 1
    }
    return result
}
```

Explanation:
The `IncrList` function takes a slice of integers `l` as input and returns a new slice with each element incremented by 1.

Here's a step-by-step breakdown:

1. Create a new slice `result` with the same length as the input slice `l`.
2. Iterate over the input slice `l` using a `for` loop with a range variable `i` and `v`.
3. For each element `v` at index `i`, increment it by 1 and assign the result to the corresponding index `i` in the `result` slice.
4. Return the `result` slice.

This function preserves the original input slice and returns a new slice with the incremented elements. Note that this function does not modify the original input slice.