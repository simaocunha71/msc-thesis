
// Return n-th Fibonacci number.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func Fib(n int) int {
    if n < 2 {
        return 1
    } else {
        return int(math.Pow(2, float64((n-1)/f))+math.Pow(3, float64((n-1)/f2)))
    }
}