Here is the solution in Go:

```go
import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    var maxPrime int
    var sum int
    for _, num := range lst {
        if isPrime(num) {
            if num > maxPrime {
                maxPrime = num
            }
        }
    }
    if maxPrime > 0 {
        sum = sumDigits(maxPrime)
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

func sumDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += int(n % 10)
        n /= 10
    }
    return sum
}
```

This solution works by first finding the largest prime number in the list, and then summing its digits. The `isPrime` function checks if a number is prime by testing if it is divisible by any number up to its square root. The `sumDigits` function sums the digits of a number by repeatedly dividing it by 10 and adding the remainder. The `Skjkasdkd` function iterates over the list, finding the largest prime number and summing its digits. If the list is empty or does not contain any prime numbers, the function returns 0. 

The time complexity of this solution is O(n * sqrt(m)), where n is the length of the list and m is the largest number in the list. This is because in the worst case, we have to check every number in the list to see if it is prime, and then sum the digits of the largest prime number. The space complexity is O(1), as we only use a constant amount of space to store the maximum prime number and the sum of its digits. 