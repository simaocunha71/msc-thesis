    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```

Note: This solution has a time complexity of O(n^2) because of the nested for loop. This means that if the input list is very large, this solution may not be optimal.

## Task 3

Implement a function that returns a slice of the first and last elements of a given slice.

```go
