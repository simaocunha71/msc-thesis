	for i := 1; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			if strings.Contains(strconv.Itoa(i), "7") {
				continue A
			}
			return 0
		}
	}
	return 0
}
