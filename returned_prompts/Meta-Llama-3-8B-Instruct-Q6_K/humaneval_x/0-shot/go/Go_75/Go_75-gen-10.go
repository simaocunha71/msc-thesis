```go
package main

import (
    "fmt"
    "math"
)

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

func IsMultiplyPrime(a int) bool {
    for i := 2; i <= a; i++ {
        for j := i; j <= a; j++ {
            for k := j; k <= a; k++ {
                if i*j*k == a && isPrime(i) && isPrime(j) && isPrime(k) {
                    return true
                }
            }
        }
    }
    return false
}

func main() {
    fmt.Println(IsMultiplyPrime(30)) // true
    fmt.Println(IsMultiplyPrime(31)) // false
}
```

This Go program checks if a given number is the product of three prime numbers. The `IsMultiplyPrime` function iterates over all possible combinations of numbers up to the given number and checks if each combination is the product of three prime numbers. The `isPrime` function checks if a number is prime by trying to divide it by all numbers up to its square root. The program then prints the results for the numbers 30 and 31. The output is `true` for 30 and `false` for 31. This solution has a time complexity of O(n^3) which is not efficient for large inputs. A more efficient solution would be to generate prime numbers and check if the given number is the product of any three prime numbers. This would have a time complexity of O(n log n) where n is the number of prime numbers up to the given number.  However, this would also require more memory to store the prime numbers.  For small inputs, this solution is sufficient.  For larger inputs, a more efficient solution would be needed.  In any case, this solution provides the correct results for the given inputs.  For example, `IsMultiplyPrime(30)` returns `true` and `IsMultiplyPrime(31)` returns `false`.  This is because 30 is the product of the prime numbers 2, 3, and 5, while 31 is not the product of three prime numbers.  This solution is also correct for all other inputs, but it is not efficient for large inputs.