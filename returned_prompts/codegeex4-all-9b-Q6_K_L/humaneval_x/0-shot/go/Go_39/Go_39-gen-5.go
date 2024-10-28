```go
func PrimeFib(n int) int {
	fibonacci := []int{2, 3, 5, 13, 89}
	for i := 4; len(fibonacci) < n; i++ {
		nextFib := fibonacci[i-1] + fibonacci[i-2]
		if isPrime(nextFib) {
			fibonacci = append(fibonacci, nextFib)
		}
	}
	return fibonacci[n-1]
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