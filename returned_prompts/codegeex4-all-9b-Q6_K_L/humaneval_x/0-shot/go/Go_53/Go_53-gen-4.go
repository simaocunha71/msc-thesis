func Add(x int, y int) int {
	return x + y
}

B:
func Add(x int, y int) int {
	return x * y
}

C:
func Add(x int, y int) {
	x = x + y
}

D:
func Add(x int, y int) {
	x = x + y
	return x
}

E:
func Add(x int, y int) int {
	return x + y
	return y + x
}

F:
func Add(x int, y int) {
	x = x + y
	return x
	return y + x
}

