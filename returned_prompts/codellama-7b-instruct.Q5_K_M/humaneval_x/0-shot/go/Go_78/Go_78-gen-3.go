	for _, v := range num {
		switch v {
		case 'A', 'B', 'C', 'D', 'E', 'F':
			switch v {
			case 'A':
				if v == 'A' {
					goto A
				}
			case 'B':
				if v == 'B' {
					goto A
				}
			case 'C':
				if v == 'C' {
					goto A
				}
			case 'D':
				if v == 'D' {
					goto A
				}
			case 'E':
				if v == 'E' {
					goto A
				}
			case 'F':
				if v == 'F' {
					goto A
				}
			}
		default:
			goto A
		}
	}
	return 0
}
