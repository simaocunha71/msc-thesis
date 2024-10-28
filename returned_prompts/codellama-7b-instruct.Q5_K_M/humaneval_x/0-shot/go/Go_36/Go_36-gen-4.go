	for i := 2; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			if strings.Contains(strconv.Itoa(i), "7") {
				goto A
			}
		}
	}
	return 0
}

