```go
func EvenOddCount(num int) [2]int {
    even := 0
    odd := 0
    for num != 0 {
        digit := num % 10
        if digit % 2 == 0 {
            even++
        } else {
            odd++
        }
        num = num / 10
    }
    return [2]int{even, odd}
}
```

This solution iterates through each digit of the input number and checks if it is even or odd. If the digit is even, the even counter is incremented, and if it is odd, the odd counter is incremented. The process is repeated until all digits of the number have been checked. Finally, the function returns a tuple containing the number of even and odd digits.