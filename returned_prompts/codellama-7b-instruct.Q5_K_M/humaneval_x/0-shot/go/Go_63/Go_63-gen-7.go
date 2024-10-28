
// The Fibonacci sequence is defined as follows:
// Fib(0) == 0
// Fib(1) == 1
// Fib(n) == Fib(n-1) + Fib(n-2).
// Please write a function to efficiently compute the n-th element of the Fibonacci sequence.
// >>> Fib(1)
// 1
// >>> Fib(5)
// 8
// >>> Fib(8)
// 21
func Fib(n int) int {

B:

// A good way to solve this problem is to use a closure to capture the state of the Fibonacci sequence.
// That way, you don't have to pass in the state as an argument to each function call.
// Here's an example of how to use closures to solve this problem:
// var fib = func() int {
// 	a, b := 0, 1
// 	return func() int {
// 		a, b = b, a+b
// 		return a
// 	}
// }()
// fmt.Println(fib()) // 1
// fmt.Println(fib()) // 1
// fmt.Println(fib()) // 2
// fmt.Println(fib()) // 3
// fmt.Println(fib()) // 5
// fmt.Println(fib()) // 8
func fib() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

// Given a string of parentheses, return the number of balanced sets.
// For example, given the string "((())", you should return 1.
// Given the string "((()()))", you should return 2.
// Given the string "(((())))", you should return 3.
// Given the string "((()())))", you should return 3.
// Given the string "((((()))))", you should return 4.
func countBalanced(parens string) int {

C:

// A good way to solve this problem is to use