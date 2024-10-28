You can use a for loop to iterate over the operations and keep track of the balance. If the balance falls below zero at any point, return true. Otherwise, return false. Here's the code:

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

This code works by starting with a balance of zero and adding each operation to the balance. If the balance ever falls below zero, it immediately returns true. If the loop finishes without the balance falling below zero, it returns false.