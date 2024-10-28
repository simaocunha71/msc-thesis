func BelowThreshold(l []int,t int) bool {
	for _,v := range l {
		if v >= t {
			return false
		}
	}
	return true
}

or

func BelowThreshold(l []int,t int) bool {
	for _,v := range l {
		if v >= t {
			return false
		}
	}
	return true
}