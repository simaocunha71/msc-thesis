	for i := 1; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			if strings.Contains(strconv.Itoa(i), "7") {
				return i
			}
		}
	}
	return 0
}





















