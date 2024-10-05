Here is a Go implementation of the CountUpTo function:

```go
func CountUpTo(n int) []int {
    if n <= 2 {
        return []int{}
    }
    primes := []int{2}
    for i := 3; i < n; i += 2 {
        isPrime := true
        for _, p := range primes {
            if i%p == 0 {
                isPrime = false
                break
            }
            if p*p > i {
                break
            }
        }
        if isPrime {
            primes = append(primes, i)
        }
    }
    return primes
}
```
This function first checks if n is less than or equal to 2, in which case it returns an empty array. It then initializes an array with the first prime number, 2, and then starts a loop from 3 to n-1. For each number, it checks if it is a prime number by dividing it by all the prime numbers in the array that are less than its square root. If the number is prime, it is appended to the array. Finally, the function returns the array of prime numbers.

The time complexity of this function is O(n^2) because for each number, it divides it by all the prime numbers in the array that are less than its square root. The space complexity is O(n) because it stores the array of prime numbers.