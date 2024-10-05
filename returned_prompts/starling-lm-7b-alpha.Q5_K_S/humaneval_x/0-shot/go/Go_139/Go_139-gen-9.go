	var result int = 1

	for i := 1; i < n; i++ {
		result *= i
	}

	return result
}























// Given a number N, find the largest power of 3 that does not exceed N
func LargestPowerOf3(n int) int {
	if n < 1 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n % 3 == 0 {
		return n / 3
	} else {
		return LargestPowerOf3(n / 3) * 3
	}
}


// Given a number N, find the largest power of 2 that does not exceed N
func LargestPowerOf2(n int) int {
	if n < 1 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n % 2 == 0 {
		return n / 2
	} else {
		return LargestPowerOf2(n / 2) * 2
	}
}


// Given a number N, find the largest power of 4 that does not exceed N
func LargestPowerOf4(n int) int {
	if n < 1 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n % 4 == 0 {
		return n / 4
	} else {
		return LargestPowerOf4(n / 4) * 4
	}
}




// Given a number N, find the largest power of 3 that divides N without a remainder
func LargestMultipleOf3(n int) int {
	if n < 1 {
		return 0
	}
	if n % 3 == 0 {
		return n / 3
	} else {
		return LargestMultipleOf3(n / 3) * 3
	