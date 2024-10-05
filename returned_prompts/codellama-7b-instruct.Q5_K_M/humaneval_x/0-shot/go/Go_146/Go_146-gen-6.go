
	for _, i := range nums {
		if i > 10 {
			if strconv.Itoa(i)[0] == "1" && strconv.Itoa(i)[len(strconv.Itoa(i))-1] == "1" {
				return 1
			} else {
				return 0
			}
		}
	}
	return 0
}
