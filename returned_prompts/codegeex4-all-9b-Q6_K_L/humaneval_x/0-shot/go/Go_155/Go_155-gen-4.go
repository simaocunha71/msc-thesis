```go
func EvenOddCount(num int) [2]int {
    s := strconv.Itoa(num)
    even, odd := 0, 0
    for _, c := range s {
        digit := int(c - '0')
        if digit%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}
```