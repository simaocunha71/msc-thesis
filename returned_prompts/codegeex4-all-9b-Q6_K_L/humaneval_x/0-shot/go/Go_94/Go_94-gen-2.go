```go
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
