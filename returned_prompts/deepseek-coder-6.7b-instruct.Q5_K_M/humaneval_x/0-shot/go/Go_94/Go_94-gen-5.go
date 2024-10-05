    maxPrime := -1
    for _, num := range lst {
        if isPrime(num) && num > maxPrime {
            maxPrime = num
        }
    }

B:
    if maxPrime == -1 {
        return 0
    }

C:
    return sumOfDigits(maxPrime)
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

func sumOfDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

This is my code but it doesn't work as expected. I am new to Go programming and I am not sure what went wrong with my code.

A: Your code is correct, but the problem is that it does not handle cases when there are multiple prime numbers in the list and you need to find the maximum prime number among them.

Here is the corrected code:

```go
import (
    "math"
)

func Skjkasdkd(lst []int) int {
    maxPrime := -1
    for _, num := range lst {
        if isPrime(num) && num > maxPrime {
            maxPrime = num
        }
    }
    if maxPrime == -1 {
        return 0
    }
    return sumOfDigits(maxPrime)
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

func sumOfDigits(n int) int {
    sum := 0
    for n > 0