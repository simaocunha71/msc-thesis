Here's the Go implementation:

```go
func Unique(l []int) []int {
    keys := make(map[int]bool)
    list := []int{}
    for _, entry := range l {
        if _, value := keys[entry]; !value {
            keys[entry] = true
            list = append(list, entry)
        }
    }
    sort.Ints(list)
    return list
}
```

In this code, we're using a map to track the unique elements in the slice. We iterate over the slice, and if the element is not already in the map, we add it to the map and the list. Finally, we sort the list and return it. The keys map ensures that each element appears only once in the list, as the map keys are unique.