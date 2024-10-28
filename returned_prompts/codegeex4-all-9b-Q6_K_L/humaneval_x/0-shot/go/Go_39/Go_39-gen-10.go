```go
func PrimeFib(n int) int {
	fib := []int{2, 3, 5, 13, 89}
	if n <= len(fib) {
		return fib[n-1]
	}
	for i := len(fib); ; i++ {
		if isPrime(fib[i-1] + fib[i-2]) {
			fib = append(fib, fib[i-1]+fib[i-2])
			if len(fib) == n {
				return fib[i]
			}
		}
	}
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
```

C:
The code seems to be correct and it should return the correct results for the given inputs.