```
func Fibfib(n int) int {
	if n <= 1 {
		return 0
	} else if n == 2 {
		return 1
	} else {
		a, b, c := 0, 0, 1
		for i := 3; i <= n; i++ {
			a, b, c = b, c, a+b+c
		}
		return c
	}
}
```



The code implements the function `Fibfib(n)` to compute the `n-th` element of the Fibfib number sequence. The function uses a loop to calculate the `n-th` element by maintaining three variables `a`, `b`, and `c` that store the last three elements of the sequence.

The function first checks if `n` is less than or equal to 1, in which case it returns 0. If `n` is equal to 2, it returns 1. Otherwise, it initializes `a`, `b`, and `c` to 0, 0, and 1 respectively, and then enters a loop that runs from 3 to `n`. In each iteration of the loop, it updates `a`, `b`, and `c` to `b`, `c`, and `a+b+c` respectively. Finally, it returns the value of `c`, which is the `n-th` element of the Fibfib sequence.

This function has a time complexity of O(n) and a space complexity of O(1), making it efficient for computing the `n-th` element of the Fibfib sequence.