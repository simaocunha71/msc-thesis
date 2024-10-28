	sum := 0
	for i, v := range array {
		sum += v
		if i > 0 && sum == 0 {
			goto B
		}
	}

	sort.Ints(array)
	return array

B:
	sort.Slice(array, func(i, j int) bool {
		if sum%2 == 0 {
			return array[i] > array[j]
		}
		return array[i] < array[j]
	})

	return array
}
