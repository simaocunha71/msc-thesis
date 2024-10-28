Here is a solution in Go:

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

This function first checks if the input list is empty. If it is, it returns nil. Then it initializes a variable `longest` with the first string in the list. It then iterates over the rest of the list, updating `longest` if it finds a string that is longer. Finally, it returns `longest`.