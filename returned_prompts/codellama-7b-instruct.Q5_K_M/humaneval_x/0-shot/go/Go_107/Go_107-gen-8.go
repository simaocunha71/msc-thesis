	even := 0
	odd := 0
	for i := 1; i < n; i++ {
		s := strconv.Itoa(i)
		if s == reverse(s) {
			if i%2 == 0 {
				even++
			} else {
				odd++
			}
		}
	}
	return [2]int{even, odd}
}

func reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}
