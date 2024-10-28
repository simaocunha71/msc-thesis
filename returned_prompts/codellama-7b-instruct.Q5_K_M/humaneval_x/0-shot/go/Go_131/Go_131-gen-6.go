	var answer int

	for n > 0 {
		if n%10 == 0 {
			n = n / 10
			continue A
		}
		answer = answer*int(strconv.Itoa(n%10)[0])
		n = n / 10
	}
	return answer
}















