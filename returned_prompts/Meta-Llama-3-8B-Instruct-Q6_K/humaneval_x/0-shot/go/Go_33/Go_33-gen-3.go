Here is a possible implementation of the `SortThird` function in Go:
```go
func SortThird(l []int) []int {
    result := make([]int, len(l))
    for i, v := range l {
        if i%3 == 0 {
            // indices divisible by 3, sort the values
            indices := make([]int, 0, len(l)/3)
            for j := 0; j < len(l); j += 3 {
                if j != i {
                    indices = append(indices, j)
                }
            }
            sort.Ints(l[indices])
            result[i] = l[indices[0]]
        } else {
            // indices not divisible by 3, copy the values
            result[i] = v
        }
    }
    return result
}
```
Here's an explanation of the implementation:

1. We create a new slice `result` with the same length as the input slice `l`.
2. We iterate over the input slice `l` using a range loop.
3. For each index `i` in the input slice, we check if it is divisible by 3 using the modulo operator `%`.
4. If `i` is divisible by 3, we create a new slice `indices` that contains the indices of the values that are not divisible by 3.
5. We sort the values in the `indices` slice using the `sort.Ints` function.
6. We set the value at index `i` in the `result` slice to the first value in the sorted `indices` slice.
7. If `i` is not divisible by 3, we simply copy the value at index `i` from the input slice to the `result` slice.
8. Finally, we return the `result` slice.

You can test this implementation using the examples you provided:
```go
func main() {
    fmt.Println(SortThird([]int{1, 2, 3})) // [1, 2, 3]
    fmt.Println(SortThird([]int{5, 6, 3, 4, 8, 9, 2})) // [2, 6, 3, 4, 8, 9, 5]
}
```
I hope this helps! Let me know if you have any questions. 😊

