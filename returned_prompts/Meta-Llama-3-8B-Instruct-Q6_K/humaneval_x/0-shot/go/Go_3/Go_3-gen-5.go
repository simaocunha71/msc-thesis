You can solve this problem using a for loop to iterate over the operations and a variable to keep track of the current balance. Here's the solution in Go:
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
Here's an explanation of the code:

1. We initialize the `balance` variable to 0, which represents the initial balance of the account.
2. We iterate over the `operations` slice using a for loop.
3. For each operation, we add the operation value to the `balance` variable. If the operation is a deposit, the value will be positive, and if it's a withdrawal, the value will be negative.
4. We check if the `balance` has fallen below 0. If it has, we immediately return `true`.
5. If we reach the end of the loop without the balance falling below 0, we return `false`.

You can test this function with the examples you provided:
```go
fmt.Println(BelowZero([]int{1, 2, 3})) // false
fmt.Println(BelowZero([]int{1, 2, -4, 5})) // true
```
I hope this helps! Let me know if you have any questions.