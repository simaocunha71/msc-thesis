
// Return n-th Fibonacci number.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func Fib(n int) int {
    var x, y, z int
	x = y = 0
	z = 1 // base case: n is 0 or 1
    
    for i := 3; i < n+1; i++ {
        // x and y should always be positive
		if (i & 1) == 1 {
            z += z*x // add in terms of x, which we have already computed
            
		} else {
            z = x + z*y // add in terms of x and y which we have already computed
        }
        
        x++
        y++
    }
    
    return z
}