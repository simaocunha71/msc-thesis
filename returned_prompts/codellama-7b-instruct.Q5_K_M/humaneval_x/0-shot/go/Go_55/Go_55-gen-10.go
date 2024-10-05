
// Return n-th Fibonacci number.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func Fib(n int) int {

    // If n is less than 2, return n.
    if n < 2 {
        return n
    }

    // Return sum of Fibonacci numbers of n-1 and n-2.
    return Fib(n-1) + Fib(n-2)
}
