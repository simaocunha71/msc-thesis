
	sort.Ints(lst)
	res := [2]interface{}{nil, nil}
	for _, v := range lst {
		if v < 0 && (res[0] == nil || v > res[0].(int)) {
			res[0] = v
		} else if v > 0 && (res[1] == nil || v < res[1].(int)) {
			res[1] = v
		}
	}
	return res
}

*/

func LargestSmallestIntegers(lst []int) (int, int) {

	var maxNegative, minPositive int = 0, 0
	isNegativePresent, isPositivePresent := false, false

	for _, v := range lst {
		if v < 0 && !isNegativePresent {
			maxNegative = v
			isNegativePresent = true
		} else if v > 0 && !isPositivePresent {
			minPositive = v
			isPositivePresent = true
		} else if v < 0 && v > maxNegative {
			maxNegative = v
		} else if v > 0 && v < minPositive {
			minPositive = v
		}
	}

	if !isNegativePresent {
		maxNegative = 0
	}
	if !isPositivePresent {
		minPositive = 0
	}

	return maxNegative, minPositive
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // (0,1)
	fmt.Println(LargestSmallestIntegers([]int{}))                 // (0,0)
	fmt.Println(LargestSmallestIntegers([]int{0}))                // (0,0)
}

/*
func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // (nil, 1)
	fmt.Println(LargestSmallestIntegers(