	for i, j := 0, 0; i < len(num); i++ {
		switch num[i] {
		case 'A':
			j = 10
		case 'B':
			j = 11
		case 'C':
			j = 12
		case 'D':
			j = 13
		case 'E':
			j = 14
		case 'F':
			j = 15
		default:
			j = int(num[i] - '0')
		}
		if j < 2 || !isPrime(j) {
			continue
		}
		//fmt.Printf("found prime %d\n", j)
		goto A
	}
	return j
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// 2, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 2