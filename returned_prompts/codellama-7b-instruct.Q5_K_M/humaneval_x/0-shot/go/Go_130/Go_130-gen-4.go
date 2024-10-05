
// This is an interview question, and the answer is "No, it's not possible to
// solve it in O(n)". The problem is that the function is defined in terms of
// itself, and the function is not constant in time. The function has to be
// computed again and again, and the time required to compute the function is
// not constant.

// A better approach is to use a memoization technique. We can create a map
// where we store the value of the function for each n. This way we can
// access the value of the function quickly.

// We can also use a dynamic programming technique. We can create a matrix
// where we store the value of the function for each n. This way we can access
// the value of the function quickly.

// The time complexity of the function is O(n^2), because we have to compute
// the function for each n.

// The space complexity of the function is O(n), because we have to store the
// value of the function for each n.

// The function is not optimized for space and time complexity.

func Tri(n int) []float64 {
	if n == 0 {
		return []float64{1}
	}
	return nil
}
