	if len(date) == 0 {
		return false
	}

	date = strings.Replace(date, "-", "", -1)

	if _, err := strconv.Atoi(date[:2]); err != nil {
		return false
	}

	if _, err := strconv.Atoi(date[2:4]); err != nil {
		return false
	}

	if _, err := strconv.Atoi(date[4:8]); err != nil {
		return false
	}

	return true
}


