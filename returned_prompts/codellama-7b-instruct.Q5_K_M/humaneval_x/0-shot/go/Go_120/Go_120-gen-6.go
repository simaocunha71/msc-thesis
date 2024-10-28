	for i := range arr {
		if arr[i] < 0 {
			continue A
		}
	}

	sort.Ints(arr)

	return arr[:k]
}
