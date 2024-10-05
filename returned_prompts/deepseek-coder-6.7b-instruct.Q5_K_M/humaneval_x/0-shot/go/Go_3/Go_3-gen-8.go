
    balance := 0
    for _, op := range operations {
        balance += op
        if balance < 0 {
            return true
        }
    }
    return false
}
```

### 2. Write a function that returns the number of prime numbers less than a given number `n`.

```go
