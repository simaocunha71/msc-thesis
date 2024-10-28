	for i := 0; ; i++ {
		a := int(math.Floor(math.Sqrt(5*float64(i)+1) - 1)) / 2
		b := int(math.Floor(math.Sqrt(5*float64(i)-1) + 1)) / 2
		if a > b {
			return i - 1
		}
		if IsPrime(a) && IsPrime(b) {
			return i
		}
	}
}

func IsPrime(n int) bool {
	for i := 2; i < n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
