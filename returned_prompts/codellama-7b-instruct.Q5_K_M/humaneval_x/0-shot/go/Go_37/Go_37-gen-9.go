	sort.Ints(l)

B:
	for i := 0; i < len(l); i++ {
		if i%2 == 0 {
			l[i] = l[i+1]
		}
	}

	return l
}
