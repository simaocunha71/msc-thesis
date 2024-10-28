
// Return n-th Fibonacci number.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func Fib(n int) int {
	if n == 1 || n == 2 {
		return 1
	}
	return Fib(n-1) + Fib(n-2)
}

