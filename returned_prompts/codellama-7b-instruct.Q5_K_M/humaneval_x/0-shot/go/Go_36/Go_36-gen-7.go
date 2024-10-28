	for i := 1; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			for _, digit := range strconv.Itoa(i) {
				if string(digit) == "7" {
					continue A
				}
			}
			return 1
		}
	}
	return 0
}
