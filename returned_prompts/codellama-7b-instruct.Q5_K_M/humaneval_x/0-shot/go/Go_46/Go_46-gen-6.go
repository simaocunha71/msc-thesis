// 0 0 2 0 8
// 1 1 3 2 14

B:

	if n == 0 {
		return 0
	}

	if n == 1 {
		return 0
	}

	if n == 2 {
		return 2
	}

	if n == 3 {
		return 0
	}

	a := 0
	b := 0
	c := 2
	d := 0

	for i := 4; i <= n; i++ {
		a = b
		b = c
		c = d
		d = a + b + c + d
	}

	return d
}

// B:
// 0 0 2 0 8
// 1 1 3 2 14

C:

	if n == 0 {
		return 0
	}

	if n == 1 {
		return 0
	}

	if n == 2 {
		return 2
	}

	if n == 3 {
		return 0
	}

	a, b, c, d := 0, 0, 2, 0

	for i := 4; i <= n; i++ {
		a = b
		b = c
		c = d
		d = a + b + c + d
	}

	return d
}

D:

	if n == 0 {
		return 0
	}

	if n == 1 {
		return 0
	}

	if n ==