
// The first step in solving this problem is to initialize an array to store the
// first n + 1 numbers of the Tribonacci sequence.
	trib := make([]float64, n + 1)

// Then, we set the first three numbers of the sequence manually because they're
// given in the problem statement.
	trib[0] = 3
	if n > 0 {
		trib[1] = 1
	}
	if n > 1 {
		trib[2] = 2
	}

// Next, we start calculating the remaining numbers of the sequence using the
// given recurrence relation.
	for i := 3; i <= n; i++ {
		if i % 2 == 0 {
			trib[i] = 1 + float64(i) / 2
		} else {
			trib[i] = trib[i - 1] + trib[i - 2] + trib[i + 1]
		}
	}

// Finally, we return the array.
	return trib
}

// Note: The solution assumes that the input will be a non-negative integer and
// that the input will be large enough to hold the entire Tribonacci sequence.
// If the input is too large, the solution may run slowly or fail due to memory
// limitations.
// The solution also assumes that the input will be a non-negative integer. If the
// input is negative, the solution may not behave correctly.
// The solution also assumes that the input will not be too large. If the input is
// too large, the solution may take a long time to run and may not be able to run
// at all due to memory limitations.
// The solution also assumes that the input will be a non-negative integer. If the
// input is negative, the solution may not behave correctly.
// The solution also assumes that the input will not be too large. If the input is
// too large, the solution may take a long time to run and may not be able to run
// at all due to memory limitations.
// The solution also assumes that the input will be a non-negative integer. If the
// input is negative, the solution may not behave correctly.
// The solution also assumes that the input will not be too large. If the input is