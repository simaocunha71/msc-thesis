	var oddList []int
	for i := 1; i < n; i++ {
		if i%2 != 0 {
			oddList = append(oddList, i)
		}
	}

	sort.Ints(oddList)
	return oddList
}