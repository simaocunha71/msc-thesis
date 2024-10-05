
    for i := 0; i < len(l); i++ {
        for j := i + 1; j < len(l); j++ {
            if l[i] + l[j] == 0 {
                return true
            }
        }
    }

    return false
}
```

- This solution works by iterating over the list with two nested loops. If it finds two distinct elements that sum to zero, it returns true. If it finishes the loops without finding such pair, it returns false.
- The time complexity of this solution is O(n^2), because it uses two nested loops, each running up to n times (where n is the length of the list).
- The space complexity is O(1), because it uses a constant amount of space to store the input and the variables i, j.


## Solution with hash map

```go
