Here is a possible solution in Go:
```go
import (
    "math"
    "strconv"
)

func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        sum := 0
        str := strconv.Itoa(abs(num))
        for _, c := range str {
            digit, _ := strconv.Atoi(string(c))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

func