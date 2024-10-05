
func CycpatternCheck(a string, b string) bool {
	var x, y string
	for i := 0; i < len(b); i++ {
		x = a
		for j := 0; j < len(b); j++ {
			x = x[1:] + x[0:1]
			y += string(x[j])
		}
		if strings.Contains(x, y) {
			return true
		}
	}
	return false
}

func CycpatternCheck(a string, b string) bool {
	return b + b[:len(b)] == a[:len(b)] + a
}

func CycpatternCheck(a string, b string) bool {
	var x, y string
	for i := 0; i < len(b); i++ {
		x = a
		for j := 0; j < len(b); j++ {
			x = x[1:] + x[0:1]
			y += string(x[j])
		}
		if strings.Contains(x, y) {
			return true
		}
	}
	return false
}
