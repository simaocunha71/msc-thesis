```go
func Skjkasdkd(lst []int) int {
    // Define a helper function to check if a number is prime
    isPrime := func(n int) bool {
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
    
    // Initialize the maximum prime value and its sum of digits
    maxPrime := 0
    sumDigits := 0
    
    // Iterate over the list to find the largest prime value
    for _, num := range lst {
        if isPrime(num) && num > maxPrime {
            maxPrime = num
        }
    }
    
    // Convert the maximum prime value to a string and calculate the sum of its digits
    sumDigitsStr := strconv.Itoa(maxPrime)
    for _, digit := range sumDigitsStr {
        digitInt, _ := strconv.Atoi(string(digit))
        sumDigits += digitInt
    }
    
    return sumDigits
}
```
