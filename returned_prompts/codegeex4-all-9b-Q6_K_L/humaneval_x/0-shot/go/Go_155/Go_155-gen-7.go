```go
func EvenOddCount(num int) [2]int {
    var evens, odds int
    if num < 0 {
        num = -num
    }
    for num > 0 {
        digit := num % 10
        if digit%2 == 0 {
            evens++
        } else {
            odds++
        }
        num /= 10
    }
    return [2]int{evens, odds}
}
```