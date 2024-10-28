
// The basic factorial function:
func Factorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * Factorial(n-1)
}

// The Brazilian factorial function:
func BrazilianFactorial(n int) int {
	if n <= 1 {
		return 1
	}
	return Factorial(n) * BrazilianFactorial(n-1)
}

return BrazilianFactorial(n)
}

