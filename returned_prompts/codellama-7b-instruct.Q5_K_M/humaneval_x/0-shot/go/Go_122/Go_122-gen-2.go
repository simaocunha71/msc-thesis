	for i := 0; i < k; i++ {
		if len(arr) < 2 {
			break A
		}
		arr[i+1] += arr[i]
	}
	return arr[k-1]
}
