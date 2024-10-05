
// To solve this problem, we can use a dynamic programming approach to solve it by storing the previously computed values in an array and using them to compute the current value.

// In this case, we initialize an array of size n+1 with all elements as 0. Then, we start populating the array from the 2nd position to the n-th position.

// For each position i, we calculate the value as the sum of the (i-1)th, (i-2)th and (i-3)th elements of the array.

// Finally, we return the n-th element of the array as the result.

B:

// Let's implement the function in Go.

func Fibfib(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }
    fib := make([]int, n+1)
    fib[0] = 0
    fib[1] = 0
    fib[2] = 1
    for i := 3; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
    }
    return fib[n]
}

C:

// Let's test the function with some test cases.

fmt.Println(Fibfib(1)) // 0
fmt.Println(Fibfib(5)) // 4
fmt.Println(Fibfib(8)) // 24

*/

package main

import (
	"fmt"
)

func Fibfib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 0
	}
	if n == 2 {
		return 1
	}
	fib := make([]int, n+1)
	fib[0] = 0
	fib[1] = 0
	fib[2] = 1
	for i := 3; i <= n; i++ {
		fib[i] = fib[i-1