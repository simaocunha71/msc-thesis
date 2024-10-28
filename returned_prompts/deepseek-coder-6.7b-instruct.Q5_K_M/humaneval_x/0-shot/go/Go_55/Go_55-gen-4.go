
}

func main()  {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib(8))
}

*/

package main

import "fmt"

func Fib(n int) int {
	if n <= 1 {
		return n
	}

	a, b := 0, 1
	for i := 2; i <= n; i++ {
		a, b = b, a+b
	}

	return b
}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib(8))
}

// 注意：此代码使用迭代的方式来计算 Fibonacci 数列，而不是递归的方式。
// 迭代方式避免了递归方式可能出现的堆栈溢出问题。
// 由于迭代方式不需要为每个递归调用创建新的堆栈帧，因此它可以处理更大的输入而不会导致堆栈溢出。
// 此外，迭代方式可以更高效地处理更大的输入，因为它避免了递归调用的开销。
// 因此，对于计算 Fibonacci 数列，迭代方式通常是更好的选择。
package main

import (
	"fmt"
	"math"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	reversed := 0
	origin := x
	for x != 0 {
		reversed = reversed*10 + x%10
		x = x / 10
	}
	return origin == reversed
}

func main() {
	fmt.Println(isPalindrome(121))  // true
	fmt.Println(isPalindrome(-121)) // false
	fmt.Println(isPalindrome(10))   // false
	fmt.Println(isPalindrome(1001)) // true
}

// 这个