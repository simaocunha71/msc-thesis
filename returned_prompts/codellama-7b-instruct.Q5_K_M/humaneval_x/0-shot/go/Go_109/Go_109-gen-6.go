	for i := len(arr) - 1; i > 0; i-- {
		if arr[i] < arr[i-1] {
			arr[i], arr[i-1] = arr[i-1], arr[i]
			sort.Ints(arr)
			continue A
		}
	}
	return true
}
