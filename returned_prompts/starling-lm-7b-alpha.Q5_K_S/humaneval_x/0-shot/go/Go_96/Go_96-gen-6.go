
```go
func CountUpTo(n int) []int {
	primes := make([]int, 0)
	for i := 2; i < n; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes
}

func isPrime(n int) bool {
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
```

In the `CountUpTo` function, we use a `for` loop to iterate through the numbers from 2 to `n-1`. For each number, we use a `if` statement to check if the number is prime. If it is, we use the `append` function to add it to the `primes` slice. Finally, we return the `primes` slice.

The `isPrime` function checks if a number is prime. It first checks if the number is less than or equal to 1, in which case it returns `false` because prime numbers are defined as positive integers greater than 1. Then, it uses a `for` loop to check if the number is divisible by any number from 2 to the square root of the number. If it is, the function returns `false`, otherwise it returns `true`.

By calling the `isPrime` function inside the `CountUpTo` function, we can determine if each number is prime and add it to the `primes` slice if it is.

Here's an example usage of the `CountUpTo` function:

```go
fmt.Println(CountUpTo(5)) // Output: [2, 3]
fmt.Println(CountUpTo(11)) // Output: [2, 3, 5, 7]
fmt.Println(CountUpTo(0)) // Output: []
fmt.Println(CountUpTo(20)) // Output: [2, 3, 5, 7, 11, 13, 1