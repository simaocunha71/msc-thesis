```go
func PrimeLength(s string) bool {
    length := len(s)
    for i := 2; i <= length; i++ {
        if length%i == 0 {
            return false
        }
    }
    return true
}
```


In this solution, we iterate through all numbers from 2 to the length of the string. If we find any number that divides the length of the string, we immediately return false because the length is not a prime number. If we don't find any such number, we return true because the length is a prime number. This approach is simple but not very efficient for large strings because it involves iterating up to the length of the string. There are more efficient algorithms for checking primality, such as the Sieve of Eratosthenes, but they are also more complex.