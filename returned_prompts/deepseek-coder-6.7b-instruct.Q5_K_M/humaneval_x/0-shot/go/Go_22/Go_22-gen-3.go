    var ints []int
    for _, value := range values {
        if val, ok := value.(int); ok {
            ints = append(ints, val)
        }
    }
    return ints
}
```

## Exercise 2

Write a function that checks if a given string is a palindrome.

```go
