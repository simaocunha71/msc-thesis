
    var result []int

    for i, num := range numbers {
        result = append(result, num)
        if i < len(numbers) - 1 {
            result = append(result, delimeter)
        }
    }

    return result
}
```

## Task 2:

Write a function `IsUnique` that takes a slice of strings and returns true if all elements in the slice are unique.

```go
