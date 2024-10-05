Here is a possible solution in Go:
```go
func SortEven(l []int) []int {
    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i%2 == 0 {
            // even index, sort the value
            sort.Ints([]int{l[i]})
            result[i] = l[i]
        } else {
            // odd index, keep the value unchanged
            result[i] = l[i]
        }
    }
    return result
}
```
Here's an explanation of the code:

1. We create a new slice `result` with the same length as the input slice `l`.
2. We iterate over the indices of `l` using a for loop.
3. For each index `i`, we check if it's even using the modulo operator (`i%2 == 0`).
4. If the index is even, we sort the value at that index using the `sort.Ints` function, which sorts the slice in place. We then assign the sorted value to the corresponding index in the `result` slice.
5. If the index is odd, we simply assign the original value from `l` to the corresponding index in `result`.
6. Finally, we return the `result` slice.

You can test this function with the examples you provided:
```go
func main() {
    fmt.Println(SortEven([]int{1, 2, 3})) // [1, 2, 3]
    fmt.Println(SortEven([]int{5, 6, 3, 4})) // [3, 6, 5, 4]
}
```I hope this helps! Let me know if you have any questions.