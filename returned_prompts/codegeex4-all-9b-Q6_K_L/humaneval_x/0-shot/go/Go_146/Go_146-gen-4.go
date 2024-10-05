```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 && isOdd(num) {
            firstDigit, lastDigit := getFirstAndLastDigits(num)
            if firstDigit%2 == 1 && lastDigit%2 == 1 {
                count++
            }
        }
    }
    return count
}

func isOdd(num int) bool {
    return num%2 == 1
}

func getFirstAndLastDigits(num int) (int, int) {
    absNum := abs(num)
    firstDigit := absNum % 10
    lastDigit := absNum / (int(math.Pow10(int(math.Log10(float64(absNum))))))
    return firstDigit, lastDigit
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}
```