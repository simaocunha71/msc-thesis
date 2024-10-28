import (
	"math"
	"sort"
)

func NextSmallest(lst []int) interface{} {
	if len(lst) < 2 {
		return nil
	}

	sort.Ints(lst)

	min := math.MaxInt
	secondMin := math.MaxInt

	for _, num := range lst {
		if num < min {
			secondMin = min
			min = num
		} else if num < secondMin && num > min {
			secondMin = num
		}
	}

	if secondMin == math.MaxInt {
		return nil
	}

	return secondMin
}