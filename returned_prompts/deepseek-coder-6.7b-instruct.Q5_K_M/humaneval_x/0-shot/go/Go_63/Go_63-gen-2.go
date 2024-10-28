
// We can solve this problem using dynamic programming.
// We define an array fibfib[n+1] to store the Fibfib number sequence.
// We initialize fibfib[0] and fibfib[1] to be 0, and fibfib[2] to be 1.
// Then for each i from 3 to n, we update fibfib[i] to be fibfib[i-1] + fibfib[i-2] + fibfib[i-3].
// Finally we return fibfib[n].

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

	fibfib := make([]int, n+1)
	fibfib[0] = 0
	fibfib[1] = 0
	fibfib[2] = 1

	for i := 3; i <= n; i++ {
		fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
	}

	return fibfib[n]
}

// Time complexity is O(n) as we iterate from 3 to n.
// Space complexity is also O(n) for the fibfib array.


// In this solution, we use an iterative approach to avoid the possibility of stack overflow that can occur when n is large.
// We only keep track of the last three values in the sequence, updating them as we go along.

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

	a, b, c := 0, 0, 1
	var d int

	for i := 3; i <= n; i++ {
		d = a + b + c
		a, b, c = b, c, d
	}

	return d
}

// Time complexity is O(n) as we iter