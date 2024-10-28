
// 1. Create a new variable to store the result.
// 2. Initialize the result to 1.
// 3. Iterate from n-1 down to 1.
// 4. Multiply the current value of the iteration by the result.
// 5. Return the result.

	result := 1
	for i := n; i > 1; i-- {
		result = result * i
	}
	return result
}
