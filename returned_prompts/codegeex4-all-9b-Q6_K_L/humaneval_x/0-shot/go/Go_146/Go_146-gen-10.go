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

func isOdd(num int) bool {
    firstDigit := num
    for firstDigit >= 10 {
        firstDigit /= 10
    }
    lastDigit := num % 10
    return firstDigit%2 == 1 && lastDigit%2 == 1
}
```