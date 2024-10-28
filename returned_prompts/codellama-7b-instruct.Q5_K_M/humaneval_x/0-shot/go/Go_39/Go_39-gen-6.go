	f := fibonacci(n)
	for {
		if isPrime(f) {
			return f
		}
		f = fibonacci(n)
	}
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i < int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func fibonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
	fmt.Println(PrimeFib(1))
	fmt.Println(PrimeFib(2))
	fmt.Println(PrimeFib(3))
}