The function ChooseNum(x, y int) int returns the largest even integer number in the range [x, y] inclusive. If there is no such number, it returns -1.

Here is the solution:
```go
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }
    for i := y; i >= x; i-- {
        if i%2 == 0 {
            return i
        }
    }
    return -1
}
```



Here is the explanation of the code:
1. The function first checks if x is greater than y. If it is, it returns -1 because there is no even integer number in the range [x, y].
2. If x is not greater than y, it then iterates through the range [x, y] from y to x in reverse order.
3. For each number i in the range, it checks if i is even by using the modulus operator (`i%2 == 0`). If i is even, it returns i as the largest even integer number in the range.
4. If the function iterates through the entire range and does not find an even integer number, it returns -1.

This function works for positive integer inputs and returns the correct results for the given examples.