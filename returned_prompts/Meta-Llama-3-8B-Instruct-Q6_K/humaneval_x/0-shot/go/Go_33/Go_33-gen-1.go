```go
func SortThird(l []int) []int {
    sortIndices := make([]int, 0)
    result := make([]int, 0)
    for i, v := range l {
        if i%3 == 0 {
            sortIndices = append(sortIndices, v)
        } else {
            result = append(result, v)
        }
    }
    sort.Ints(sortIndices)
    for i, v := range l {
        if i%3 == 0 {
            result[i] = v
        }
    }
    return result
}
```
In this solution, we first create two slices: `sortIndices` to store the values that need to be sorted, and `result` to store the final result. We then iterate over the input list `l`, and for each value, we check if its index is divisible by 3. If it is, we add the value to `sortIndices`; otherwise, we add it to `result`. After that, we sort `sortIndices` using `sort.Ints`. Finally, we iterate over `l` again, and for each value, if its index is divisible by 3, we replace the corresponding value in `result` with the sorted value from `sortIndices`. The final result is returned.