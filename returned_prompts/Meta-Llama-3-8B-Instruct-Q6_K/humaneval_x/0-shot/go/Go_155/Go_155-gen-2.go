Here is the solution:
```go
import (
    "strconv"
)

func EvenOddCount(num int) [2]int {
    evenCount := 0
    oddCount := 0
    strNum := strconv.Itoa(abs(num))
    for _, c := range strNum {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```
This solution converts the integer to a string, then iterates over each character (digit) in the string. It converts each character back to an integer, checks if it's even or odd, and increments the corresponding counter. Finally, it returns a tuple (array) with the even and odd counts.

Note: The `abs` function is used to handle negative numbers. If the input number is negative, the function returns its absolute value. This is because the problem statement doesn't specify what to do with negative numbers, so I chose to ignore the sign and treat negative numbers as positive for the purpose of counting even and odd digits. If you want to include the sign in the output, you can modify the function accordingly.