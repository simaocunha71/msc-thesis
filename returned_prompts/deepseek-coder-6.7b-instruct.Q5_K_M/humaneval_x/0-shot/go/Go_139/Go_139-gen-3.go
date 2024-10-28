
    // Your code here
    if n==0 {
        return 1
    }
    result := 1
    for i:=1; i<=n; i++ {
        result *= factorial(i)
    }
    return result
}

func factorial(n int) int {
    if n < 2 {
        return 1
    }
    return n * factorial(n-1)
}

func main() {
    fmt.Println(SpecialFactorial(4)) // 288
}
*/

import "fmt"

func SpecialFactorial(n int) int {
	if n == 0 {
		return 1
	}
	result := 1
	for i := 1; i <= n; i++ {
		result *= Factorial(i)
	}
	return result
}

func Factorial(n int) int {
	if n < 2 {
		return 1
	}
	return n * Factorial(n-1)
}

func main() {
	fmt.Println(SpecialFactorial(4)) // 288
}

// The function works by calling a helper function, Factorial, to calculate the factorial of each number up to n.
// The factorial of each number is then multiplied together to give the final result.
// This is the definition of the "Brazilian factorial" or "special factorial".
// For example, SpecialFactorial(4) calculates 4*3*2*1 * 3*2*1 * 2*1 * 1, which equals 288.
// The base case for the recursive Factorial function is n < 2, returning 1 for n=0 and n=1,
// because 0 and 1 factorial is 1. For n > 1, the function returns n * Factorial(n-1),
// which is the standard definition of the factorial function.
// This recursive definition allows the calculation of the factorial for any positive integer n.
// The time complexity of the function is O(n), and the space complexity is O(n),
// because each recursive call adds a layer to the call stack.
// In terms of performance, this