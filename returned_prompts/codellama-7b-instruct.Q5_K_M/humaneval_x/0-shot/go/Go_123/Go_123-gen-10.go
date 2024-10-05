	if n < 1 {
		return nil
	}
	
	list := []int{}
	for n > 1 {
		if n%2 == 0 {
			n = n / 2
		} else {
			n = 3*n + 1
		}
		list = append(list, n)
	}
	sort.Ints(list)
	return list
}

