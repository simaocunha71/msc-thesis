
// Base case: if n is 0 or 1, return n.
if n <= 1 {
return n
}

// Recursive case: return the sum of the (n-1)th and (n-2)th Fibonacci numbers.
return Fib(n-1) + Fib(n-2)
}
*/

func Fib(n int) int {
	if n <= 1 {
		return n
	}

	return Fib(n-1) + Fib(n-2)
}

// FibDP is a solution using dynamic programming.
func FibDP(n int) int {
	if n <= 1 {
		return n
	}

	// Initialize a slice to store the Fibonacci numbers.
	Fib := make([]int, n+1)

	// Base case: Fibonacci of 0 and 1 is 0 and 1 respectively.
	Fib[0], Fib[1] = 0, 1

	// Dynamic programming approach: store the Fibonacci numbers in the slice.
	for i := 2; i <= n; i++ {
		Fib[i] = Fib[i-1] + Fib[i-2]
	}

	return Fib[n]
}

// FibDP2 is a solution using dynamic programming with O(1) space.
func FibDP2(n int) int {
	if n <= 1 {
		return n
	}

	// Initialize variables to store the last two Fibonacci numbers.
	a, b := 0, 1

	// Dynamic programming approach: store the Fibonacci numbers in the variables.
	for i := 2; i <= n; i++ {
		a, b = b, a+b
	}

	return b
}

// FibDP3 is a solution using matrix exponentiation.
func FibDP3(n int) int {
	if n <= 1 {
		return n
	}

	// Initialize a matrix to represent the Fibonacci sequence.
	Fib := [][]int{{0, 1}, {1, 1}}

	//