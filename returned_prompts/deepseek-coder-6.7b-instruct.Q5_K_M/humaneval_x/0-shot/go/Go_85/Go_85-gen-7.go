
    sum := 0

    for i, num := range lst {
        if i % 2 != 0 && num % 2 == 0 {
            sum += num
        }
    }

    return sum
}

// This function works by iterating over the list of numbers. It uses the range keyword to get both the index and value of each number.
// If the index is odd (i % 2 != 0) and the number is even (num % 2 == 0), it adds the number to the sum.
// Finally, it returns the sum.

```

## 6. Simple Fun #176: Reverse Letter

```go
