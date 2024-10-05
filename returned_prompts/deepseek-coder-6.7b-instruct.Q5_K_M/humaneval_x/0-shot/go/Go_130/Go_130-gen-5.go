
	seq := make([]float64, n + 1)

B:

	seq[0] = 3

C:

	if n == 0 {
		return seq
	}

D:

	seq[1] = 3

E:

	if n == 1 {
		return seq
	}

F:

	seq[2] = 2

G:

	for i := 3; i <= n; i++ {
		if i % 2 == 0 {
			seq[i] = 1 + float64(i) / 2
		} else {
			seq[i] = seq[i-1] + seq[i-2] + seq[i+1]
		}
	}

H:

	return seq

}

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end

// end