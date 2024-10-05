	for _, v := range []byte(num) {
		switch v {
		case 'A':
			fallthrough
		case 'B':
			fallthrough
		case 'D':
			fallthrough
		case 'E':
			fallthrough
		case 'F':
			continue A
		}
		if isPrime(v) {
			return 1
		}
	}
	return 0
}

func isPrime(num byte) bool {
	switch num {
	case '2':
		return true
	case '3':
		return true
	case '5':
		return true
	case '7':
		return true
	case 'B':
		return true
	case 'D':
		return true
	default:
		return false
	}
}
