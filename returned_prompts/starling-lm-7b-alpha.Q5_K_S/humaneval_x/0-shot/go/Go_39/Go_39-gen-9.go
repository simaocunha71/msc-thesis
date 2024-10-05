	if n == 1 {
		return 2
	}

	i := 3
	f1 := 1
	f2 := 2
	for i < n {
		f := f1 + f2
		if f%2 == 0 {
			continue
		}
		if f > n {
			break
		}
		if math.Sqrt(f)%1 != 0 {
			continue
		}
		for i < n {
			f = f1 + f2
			if f%2 == 0 {
				continue
			}
			if f > n {
				break
			}
			if math.Sqrt(f)%1 != 0 {
				break
			}
			if f == n {
				return f
			}
		}
		f1 = f2
		f2 = f
		i++
	}
	return f2
}






















































































































































































































































