	for i := 0; i < k; i++ {
		if len(strconv.Itoa(arr[i])) > 2 {
			continue A
		}
	}

	var sum int
	for i := 0; i < k; i++ {
		sum += arr[i]
	}
	return sum
}


