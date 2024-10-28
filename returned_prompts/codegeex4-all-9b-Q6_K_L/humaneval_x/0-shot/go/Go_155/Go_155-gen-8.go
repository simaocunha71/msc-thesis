```go
func EvenOddCount(num int) [2]int {
    num = abs(num)
    even := 0
    odd := 0
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

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}
```
This solution works by iterating over the digits of the input number and counting the number of even and odd digits. The function `abs` is used to convert the input number to a positive integer if it is negative.