Here is the solution:
```go
import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    maxPrime := 0
    for _, num := range lst {
        if isPrime(num) && num > maxPrime {
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

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```
This solution first finds the largest prime number in the list, and then calculates the sum of its digits. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it has any divisors. If it has no divisors, it is a prime number. The `Skjkasdkd` function then converts the largest prime number to a string, iterates over each character (digit), and adds it to the sum. Finally, it returns the sum. If the largest prime number is 0, it returns 0.