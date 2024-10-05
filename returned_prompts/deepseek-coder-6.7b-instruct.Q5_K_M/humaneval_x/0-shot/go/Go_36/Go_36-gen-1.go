	count := 0
	strN := strconv.Itoa(n)

B:
	for i := 0; i < n; i++ {
		if i % 11 == 0 || i % 13 == 0 {
			