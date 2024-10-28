```go
func EvenOddCount(num int) [2]int {
    var even, odd int
    absNum := abs(num)
    for absNum > 0 {
        digit := absNum % 10
        if digit % 2 == 0 {
            even++
        } else {
            odd++
        }
        absNum /= 10
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

This solution works by first taking the absolute value of the input number. Then, it iterates through each digit of the number, checking if it is even or odd. The count of even and odd digits is kept track of using the `even` and `odd` variables. Finally, the counts are returned as a tuple.