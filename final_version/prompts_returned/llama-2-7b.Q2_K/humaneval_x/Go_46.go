
// The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
// Fib4(0) -> 0
// Fib4(1) -> 0
// Fib4(2) -> 2
// Fib4(3) -> 0
// Fib4(n) -> Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4).
// Please write a function to efficiently compute the n-th element of the Fib4 number sequence.  Do not use recursion.
// >>> Fib4(5)
// 4
// >>> Fib4(6)
// 8
// >>> Fib4(7)
// 14
func Fib4(n int) int {
	if n < 2 || n == 0 {
		return 0;
	} else {
		var a, b, c = n - 1, i = n - 3;
		for ;i >= 3 && i <= n-4;i-- {
			c = (a + b) / 2
			b += c
			a = c
		}
		return a+b+c;
	}
}