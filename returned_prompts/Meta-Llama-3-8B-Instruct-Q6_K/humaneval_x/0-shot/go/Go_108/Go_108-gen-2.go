Here is the solution in Go:

```go
import (
    "math"
    "strconv"
)

func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        sum := 0
        for _, ch := range strconv.Itoa(abs(num)) {
            digit, _ := strconv.Atoi(string(ch))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

In this solution, we iterate over each number in the array. For each number, we calculate the sum of its digits using a second loop that converts the number to a string and then iterates over each character in the string. We use the `abs` function to handle negative numbers. If the sum of the digits is greater than 0, we increment the count. Finally, we return the count.