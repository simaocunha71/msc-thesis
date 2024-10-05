
	if len(q) < 2 {
		return false
	}

	for i := 0; i < len(q)/2; i++ {
		if q[i] != q[len(q)-1-i] {
			return false
		}
	}

	if sum := 0; sum < w {
		for _, v := range q {
			sum += v
		}
		return sum <= w
	}
	return false

}
