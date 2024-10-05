Here's how you can sort the even indices of a list in Go:

```go
func SortEven(l []int) []int {
    // Extract the even indices
    evens := []int{}
    for i := 0; i < len(l); i += 2 {
        evens = append(evens, l[i])
    }
    
    // Sort the extracted even indices
    sort.Ints(evens)
    
    // Reinsert the sorted even indices back into the original list
    for i := 0; i < len(evens); i++ {
        l[i*2] = evens[i]
    }
    
    return l
}
```

This function first extracts the even indices of the given list. It then sorts these indices and finally inserts them back into the original list at the even indices. This way, the original list is modified to have the sorted even indices.