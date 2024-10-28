func PrimeFib(n int) int {
	if n <= 0 {
		return 0
	}

	// Initialize the first two Fibonacci numbers
	var a, b int = 1, 1
	var count int = 0

	// Loop until we find the n-th prime Fibonacci number
	for {
		// Calculate the next Fibonacci number
		next := a + b

		// Check if the next Fibonacci number is prime
		if isPrime(next) {
			count++
		}

		// Check if we have found the n-th prime Fibonacci number
		if count == n {
			return next
		}

		// Update the Fibonacci numbers
		a = b
		b = next
	}
}

// isPrime checks if a number is prime
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}

	// Check if n is divisible by any number up to the square root of n
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}

// Test code
func main() {
	for i := 1; i <= 5; i++ {
		println(PrimeFib(i))
	}
}