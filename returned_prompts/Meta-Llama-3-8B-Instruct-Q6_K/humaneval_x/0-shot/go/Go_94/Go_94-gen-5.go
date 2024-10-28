Here is a possible solution to the problem:

```go
import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    var maxPrime int
    for _, num := range lst {
        if num < 2 {
            continue
        }
        isPrime := true
        for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
            if num%i == 0 {
                isPrime = false
                break
            }
        }
        if isPrime && num > maxPrime {
            maxPrime = num
        }
    }
    if maxPrime == 0 {
        return 0
    }
    sum := 0
    for _, digit := range strconv.Itoa(maxPrime) {
        sum += int(digit - '0')
    }
    return sum
}
```

This function iterates over the input list, checks each number to see if it is prime, and keeps track of the largest prime number found. It then converts the largest prime number to a string, iterates over the digits, and sums them up. The sum is returned as the result. If the input list is empty, the function returns 0. If the largest prime number is 0, the function also returns 0. Otherwise, it returns the sum of the digits of the largest prime number.