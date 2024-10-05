```go
func EvenOddCount(num int) [2]int {
    var evenCount, oddCount int
    num = abs(num)
    for _, digit := range strconv.Itoa(num) {
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}
```
