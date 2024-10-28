    result := 0
    for i := 11; i < n; i += 11, result += count_7(i)
    for i := 13; i < n; i += 13, result += count_7(i)
    return result
}

func count_7(n int) int {
	var result := 0
	for _, s := range strings.Split(strconv.Itoa(n), "7") {
		if len(s) > 0 {
			result += len(s)
		}
	}
	return result
}



