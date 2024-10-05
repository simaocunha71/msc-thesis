```go
func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        if sumDigits(num) > 0 {
            count++
        }
    }
    return count
}

func sumDigits(num int) int {
    sum := 0
    absNum := int(math.Abs(float64(num)))
    for absNum != 0 {
        sum += absNum % 10
        absNum /= 10
    }
    return sum
}
```