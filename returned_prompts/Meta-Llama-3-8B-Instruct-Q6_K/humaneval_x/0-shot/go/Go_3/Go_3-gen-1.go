```
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


Explanation:
The function `BelowZero` takes a list of integers as input, representing the deposit and withdrawal operations on a bank account. It starts with a balance of zero and then iterates over the operations. For each operation, it adds the amount to the balance. If the balance ever falls below zero, it immediately returns `true`. If it finishes iterating over all operations without the balance falling below zero, it returns `false`. This solution has a time complexity of O(n), where n is the number of operations, because it iterates over the operations once. It also uses a constant amount of space, so its space complexity is O(1).