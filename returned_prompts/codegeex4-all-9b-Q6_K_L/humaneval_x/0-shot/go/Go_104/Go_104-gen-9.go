```go
func UniqueDigits(x []int) []int {
    result := []int{}
    for _, num := range x {
        if hasEvenDigit(num) {
            continue
        }
        result = append(result, num)
    }
    sort.Ints(result)
    return result
}

func hasEvenDigit(num int) bool {
    for num > 0 {
        digit := num % 10
        if digit%2 == 0 {
            return true
        }
        num /= 10
    }
    return false
}
```
