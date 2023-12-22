
// You're given a list of deposit and withdrawal operations on a bank account that starts with
// zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
// at that point function should return true. Otherwise it should return false.
// >>> BelowZero([1, 2, 3])
// false
// >>> BelowZero([1, 2, -4, 5])
// true
func BelowZero(operations []int) bool {
    balance := 0
    for _, operation := range operations {
        switch op{
             case Withdrawal:
                balance = balance - operation
             case Deposit:
                balance = balance + operation
        }
    }
    return balance < 0
}