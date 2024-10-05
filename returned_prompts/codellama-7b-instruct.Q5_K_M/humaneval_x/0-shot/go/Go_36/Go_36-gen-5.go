	for i := 11; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			for j := 0; j < len(strconv.Itoa(i)); j++ {
				if strconv.Itoa(i)[j] == "7" {
					continue A
				}
			}
			return strings.Count(strconv.Itoa(i), "7")
		}
	}
	return 0
}
