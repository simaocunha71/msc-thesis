```go
func Skjkasdkd(lst []int) int {
    maxPrime := 0
    for _, num := range lst {
        if num > maxPrime && isPrime(num) {
            maxPrime = num
        }
    }
    return sumDigits(maxPrime)
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

func sumDigits(num int) int {
    sum := 0
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}
```