
    if len(strings) == 0 {
        return nil
    }

    longest := strings[0]

    for _, str := range strings {
        if len(str) > len(longest) {
            longest = str
        }
    }

    return longest
}

```

## Task 2

Write a function `Average` that calculates the average of a slice of integers. If the slice is empty, the function should return 0.

Example:

```go
func Average(numbers []int) float64 {
    // Your code here
}
```

**Solution:**

```go
