```go
func SortThird(l []int) []int {
    // Create a slice of values at indices divisible by 3
    thirdValues := make([]int, 0)
    for i := 2; i < len(l); i += 3 {
        thirdValues = append(thirdValues, l[i])
    }
    // Sort the slice
    sort.Ints(thirdValues)
    // Place sorted values back into the slice
    for i, v := range thirdValues {
        l[i*3+2] = v
    }
    return l
}
```