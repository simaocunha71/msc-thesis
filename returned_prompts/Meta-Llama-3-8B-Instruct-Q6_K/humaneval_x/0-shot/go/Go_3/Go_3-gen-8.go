Here is a simple solution in Go:
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
Here's an explanation of the code:

* We initialize the `balance` variable to 0, which represents the initial balance of the account.
* We iterate through the `operations` slice using a range loop.
* For each operation, we add it to the `balance`.
* If the `balance` ever falls below 0, we immediately return `true`, indicating that the account balance has fallen below zero at some point.
* If we reach the end of the loop without the balance falling below zero, we return `false`.

You can test this function with the examples you provided:
```go
fmt.Println(BelowZero([]int{1, 2, 3})) // false
fmt.Println(BelowZero([]int{1, 2, -4, 5})) // true
```