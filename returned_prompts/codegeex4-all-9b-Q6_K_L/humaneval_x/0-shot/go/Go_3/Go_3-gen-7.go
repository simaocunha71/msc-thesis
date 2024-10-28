The function BelowZero takes in a slice of integers called operations. It then iterates through each operation in the slice, adding it to a running total called balance. If the balance ever falls below zero, the function returns true. If the balance never falls below zero, the function returns false after the loop has completed.

Here's the code:

```go
func BelowZero(operations []int) bool {
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

This function can be used to detect if the balance of an account falls below zero at any point in a series of deposit and withdrawal operations.