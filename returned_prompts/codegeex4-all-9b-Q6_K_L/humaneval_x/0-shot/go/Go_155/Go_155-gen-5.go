```go
func EvenOddCount(num int) [2]int {
    var odd, even int
    absNum := abs(num)
    for absNum > 0 {
        digit := absNum % 10
        if digit%2 == 0 {
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
