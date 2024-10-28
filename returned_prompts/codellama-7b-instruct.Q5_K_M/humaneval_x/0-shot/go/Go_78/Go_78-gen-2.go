	for i := 0; i < len(num); i++ {
		switch num[i] {
		case 'A':
			fallthrough
		case 'B':
			fallthrough
		case 'C':
			fallthrough
		case 'D':
			fallthrough
		case 'E':
			fallthrough
		case 'F':
			goto A
		}
	}
	return 0
}
