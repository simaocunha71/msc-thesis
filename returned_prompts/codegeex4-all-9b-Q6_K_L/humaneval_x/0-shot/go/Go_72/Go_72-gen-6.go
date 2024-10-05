package kata

func WillItFly(q []int, w int) bool {

	if len(q) == 0 {
		return false
	}

	var sum int
	for _, v := range q {
		sum += v
		if sum > w {
			return false
		}
	}

	for i := 0; i < len(q)/2; i++ {
		if q[i] != q[len(q)-1-i] {
			return false
		}
	}

	return true
}