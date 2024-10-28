```go
func EvenOddCount(num int) [2]int {
    var even, odd int
    if num < 0 {
        num = -num
    }
    for num > 0 {
        digit := num % 10
        if digit % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return [2]int{even, odd}
}
```