```go
func Specialfilter(nums []int) int {
    count := 0

    for _, num := range nums {
        if num > 10 && isOdd(num) {
            if isOddFirstLastDigit(num) {
                count++
            }
        }
    }

    return count
}

func isOdd(n int) bool {
    return n%2 != 0
}

func isOddFirstLastDigit(n int) bool {
    firstDigit := n % 10
    lastDigit := n

    for lastDigit >= 10 {
        lastDigit /= 10
    }

    return isOdd(firstDigit) && isOdd(lastDigit)
}
```

Explanation:
The `Specialfilter` function iterates over each number in the input array. If a number is greater than 10 and its first digit is odd, the function checks if the last digit is also odd. If both conditions are met, the count is incremented by 1. Finally, the function returns the count of numbers that meet the criteria.