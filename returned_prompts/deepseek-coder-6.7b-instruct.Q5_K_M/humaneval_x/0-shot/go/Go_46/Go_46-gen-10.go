
// Answer:

func Fib4(n int) int {
	if n <= 1 {
		return 0
	}
	if n == 2 {
		return 2
	}
	if n == 3 {
		return 0
	}

	a, b, c, d := 0, 0, 2, 0
	var next int
	for i := 4; i <= n; i++ {
		next = a + b + c + d
		a, b, c, d = b, c, d, next
	}
	return next
}

// Explanation:

// This function uses a dynamic programming approach to compute the n-th Fib4 number. The approach involves storing the last 4 numbers in the sequence and using them to compute the next number.
// By using a for loop, we iteratively compute the next number in the sequence by adding the last 4 numbers.
// The variables a, b, c, d and next are used to store the last 4 numbers and the next number in the sequence respectively.
// The function returns the next number in the sequence which is the n-th Fib4 number.

// The time complexity of this function is O(n) as it iteratively computes the next number in the sequence n times. The space complexity is O(1) as it only uses a constant amount of space to store the last 4 numbers and the next number in the sequence.

// The function works correctly for all positive integer inputs of n. For n = 0 and n = 1, the function returns 0, for n = 2, the function returns 2 and for n = 3, the function returns 0. For n > 3, the function computes the n-th Fib4 number by iteratively adding the last 4 numbers.

// Therefore, this function meets the requirements of the problem.

// I hope this explanation is clear. If you have any questions, feel free to ask.

// Good luck with your coding interview preparation.

// 