
// Define a slice to hold the Tribonacci sequence
	trib := make([]float64, n + 1)

B:

// Base cases
	trib[0] = 3
	if n > 0 {
		trib[1] = 3
		if n > 1 {
			trib[2] = 2
		}
	}

C:

// Generate the rest of the sequence
	for i := 3; i <= n; i++ {
		if i % 2 == 0 {
			trib[i] = 1 + float64(i) / 2
		} else {
			trib[i] = trib[i-1] + trib[i-2] + trib[i+1]
		}
	}

D:

// Return the sequence
	return trib
}

