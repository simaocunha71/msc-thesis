Here is a possible solution in Go:

```go
func Longest(strings []string) interface{}{
    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}
```

This solution first checks if the input list is empty, in which case it returns `nil`. Then it initializes `longest` with the first element of the list. It then iterates over the remaining elements of the list and updates `longest` if it finds an element with a greater length. Finally, it returns `longest`.