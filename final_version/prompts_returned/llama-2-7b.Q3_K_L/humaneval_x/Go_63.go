
// The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
// Fibfib(0) == 0
// Fibfib(1) == 0
// Fibfib(2) == 1
// Fibfib(n) == Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3).
// Please write a function to efficiently compute the n-th element of the Fibfib number sequence.
// >>> Fibfib(1)
// 0
// >>> Fibfib(5)
// 4
// >>> Fibfib(8)
// 24
func Fibfib(n int) int {
	if n < 3 {
		return 0
	} else if n >= 21 && n <= 29 {
		return fibfib[n-20][2] + fibfib[n-20][1] + fibfib[n-20][0]
	} else if n < 30 && n > 18 {
		a, b := fibfib[n-19][2], fibfib[n-19][1]
		return a + b
	} else if n < 50 && n >= 27 {
		return fibfib(int(n/3)) + fibfib(int((n - (float64(n/3))%3)/2)) + fibfib(int((n-1-(float64(n/3)-(float64(n-1)/2))%3)))
	} else {
		return n * int(math.Sqrt(5*n+1)) / 2.0
	}
}