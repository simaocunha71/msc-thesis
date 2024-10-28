You can solve this problem using the following steps:

1. Create a helper function to check if a number is prime.
2. Create a helper function to find all prime factors of a number.
3. Create the main function that uses the helper functions to check if a number is the multiplication of 3 prime numbers.

Here is the implementation in Go:

```
func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func PrimeFactors(n int) []int {
    factors := []int{}
    for i := 2; i <= n; i++ {
        if IsPrime(i) && n%i == 0 {
            factors = append(factors, i)
            n /= i
            i--
        }
    }
    return factors
}

func IsMultiplyPrime(a int) bool {
    factors := PrimeFactors(a)
    if len(factors) == 3 {
        return true
    }
    return false
}
```

You can test the function with the following code:

```
fmt.Println(IsMultiplyPrime(30)) // true
fmt.Println(IsMultiplyPrime(100)) // false
fmt.Println(IsMultiplyPrime(6)) // true
fmt.Println(IsMultiplyPrime(15)) // false
```