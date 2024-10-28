
func ChooseNum(x, y int) int {

	if x > y {
		return -1
	}

	if x%2 == 0 {
		return x
	}

	for x < y {
		x += 2
	}

	if x > y {
		return -1
	}

	return x
}

// B:

func ChooseNum(x, y int) int {

	if x > y {
		return -1
	}

	if x%2 == 0 && y%2 == 0 {
		return (x + y) / 2
	}

	for x < y {
		x += 2
	}

	if x > y {
		return -1
	}

	return x
}

// C:

func ChooseNum(x, y int) int {

	if x > y {
		return -1
	}

	if x%2 == 0 && y%2 == 0 {
		return (x + y) / 2
	}

	if x%2 == 0 {
		return x
	}

	for x < y {
		x += 2
	}

	if x > y {
		return -1
	}

	return x
}

// D:

func ChooseNum(x, y int) int {

	if x > y {
		return -1
	}

	if x%2 == 0 && y%2 == 0 {
		return (x + y) / 2
	}

	for x < y {
		x += 2
	}

	if x > y {
		return -1
	}

	return x
}