	// your code here
	var y []int
	for _, v := range x {
		s := strconv.Itoa(v)
		for i := 0; i < len(s); i++ {
			if s[i]%2 == 0 {
				continue A
			}
		}
		y = append(y, v)
	}
	sort.Ints(y)
	return y
}
