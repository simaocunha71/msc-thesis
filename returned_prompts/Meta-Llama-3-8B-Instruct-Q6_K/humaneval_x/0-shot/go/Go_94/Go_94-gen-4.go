Here is a Go function that solves the problem. It first filters the list to get only the prime numbers, then finds the largest one, and finally calculates the sum of its digits.

```go
import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    var maxPrime int
    var maxPrimeSum int
    for _, num := range lst {
        if num > 1 {
            isPrime := true
            for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
                if num%i == 0 {
                    isPrime = false
                    break
                }
            }
            if isPrime {
                if num > maxPrime {
                    maxPrime = num
                    maxPrimeSum = 0
                }
                sum, _ := strconv.Atoi(strconv.Itoa(num))
                sumDigits := 0
                for sum > 0 {
                    sumDigits += sum % 10
                    sum /= 10
                }
                if sumDigits > maxPrimeSum {
                    maxPrimeSum = sumDigits
                }
            }
        }
    }
    return maxPrimeSum
}
```

This function iterates over the list, checks if each number is prime, and if it is, checks if it is larger than the current maximum prime. If it is, it updates the maximum prime and its digit sum. Finally, it returns the digit sum of the maximum prime. 

The function `strconv.Itoa(num)` is used to convert the number to a string, and then `strconv.Atoi` is used to convert the string back to an integer. This is used to calculate the sum of the digits of the number. 

The function `math.Sqrt` is used to calculate the square root of the number, which is used in the prime checking loop. 

The loop `for sum > 0` is used to calculate the sum of the digits of the number. It subtracts the last digit of the number from the number, adds the last digit to the sum, and repeats this process until the number becomes 0. 

The function returns the sum of the digits of the maximum prime number. 

Please note that this function is not efficient for large lists of numbers, because it checks every number for primality. If you need to handle large lists, you may want to use a more efficient algorithm, such as the Sieve of Eratosthenes. 

Also, please note that this function does not handle the case