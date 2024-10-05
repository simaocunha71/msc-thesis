```go
func UniqueDigits(x []int) []int {
    result := []int{}
    for _, num := range x {
        hasEvenDigit := false
        for _, digit := range strconv.Itoa(num) {
            if digit%2 == 0 {
                hasEvenDigit = true
                break
            }
        }
        if !hasEvenDigit {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}
```