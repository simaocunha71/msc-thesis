```go
func UniqueDigits(x []int) []int {
    res := []int{}
    for _, i := range x {
        if hasEvenDigit(i) {
            continue
        }
        res = append(res, i)
    }
    sort.Ints(res)
    return res
}

func hasEvenDigit(n int) bool {
    for n > 0 {
        digit := n % 10
        if digit%2 == 0 {
            return true
        }
        n /= 10
    }
    return false
}
```