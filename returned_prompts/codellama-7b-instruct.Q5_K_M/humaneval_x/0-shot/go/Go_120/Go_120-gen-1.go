	if len(arr) < k {
		return arr
	}

	sort.Ints(arr)

	arr = arr[len(arr)-k:]

	return arr
}
