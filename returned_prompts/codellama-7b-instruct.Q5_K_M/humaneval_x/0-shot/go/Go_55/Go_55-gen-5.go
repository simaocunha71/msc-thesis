
// Return n-th Fibonacci number.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func Fib(n int) int {

	a, b := 1, 1
	for i := 2; i < n; i++ {
		a, b = b, a+b
	}
	return a
}
