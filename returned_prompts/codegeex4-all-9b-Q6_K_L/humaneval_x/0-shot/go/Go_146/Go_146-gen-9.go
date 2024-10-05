```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 && isOdd(num) {
            count++
        }
    }
    return count
}

func isOdd(n int) bool {
    firstDigit := n % 10
    lastDigit := n
    for lastDigit >= 10 {
        lastDigit /= 10
    }
    return firstDigit%2 == 1 && lastDigit%2 == 1
}
```
