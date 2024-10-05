for {
	fib := Fibonacci(n)
	if IsPrime(fib) {
		return fib
	}
	n++
}

func Fibonacci(n int) int {
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	return a
}

func IsPrime(n int) bool {
	if n == 1 || n == 0 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeFib(1))
}



