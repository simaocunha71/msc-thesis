Here is a solution in Go:

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 && isOdd(num) && isOddFirstAndLast(num) {
            count++
        }
    }
    return count
}

func isOdd(n int) bool {
    return n%2 != 0
}

func isOddFirstAndLast(n int) bool {
    firstDigit := int(math.Abs(float64(n))) % 10
    lastDigit := n % 10
    return firstDigit%2 != 0 && lastDigit%2 != 0
}
```

In this solution, `Specialfilter` function iterates over the input array `nums`, and for each number, it checks two conditions:

- The number is greater than 10.
- The first and last digits of the number are both odd.

The helper functions `isOdd` and `isOddFirstAndLast` are used to check if a number is odd and if the first and last digits of a number are both odd, respectively.

The function `Specialfilter` returns the count of numbers that satisfy both conditions.