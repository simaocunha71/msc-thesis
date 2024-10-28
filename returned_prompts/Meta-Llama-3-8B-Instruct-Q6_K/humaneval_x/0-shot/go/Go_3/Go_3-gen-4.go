You can solve this problem by initializing a variable `balance` to 0 and then iterating over the operations array. For each operation, you add the value to the `balance`. If the `balance` ever becomes negative, you return `true`. If you finish the loop without returning `true`, you return `false`. Here is the code:

```go
func BelowZero(operations []int) bool {
    balance := 0
    for _, operation := range operations {
        balance += operation
        if balance < 0 {
            return true
        }
    }
    return false
}
```

This solution has a time complexity of O(n), where n is the number of operations, because it needs to iterate over the entire array once. The space complexity is O(1), because it only uses a constant amount of space to store the balance and the operation.