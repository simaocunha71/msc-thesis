```go
func SortThird(l []int) []int {
    // Create a slice to hold the values at indices divisible by 3
    thirdIndices := make([]int, 0)
    // Iterate over the list and collect values at indices divisible by 3
    for i, v := range l {
        if i%3 == 0 {
            thirdIndices = append(thirdIndices, v)
        }
    }
    // Sort the collected values
    sort.Ints(thirdIndices)
    // Replace the values at indices divisible by 3 with the sorted values
    for i, v := range thirdIndices {
        l[i*3] = v
    }
    return l
}
```
