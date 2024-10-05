import (
	"math"
)

func NextSmallest(lst []int) interface{} {
	if len(lst) < 2 {
		return nil
	}

	sort.Ints(lst)
	var smallest, secondSmallest int
	for _, v := range lst {
		if v != smallest {
			if secondSmallest == 0 {
				secondSmallest = v
				break
			}
			smallest = v
		}
	}

	if secondSmallest == 0 {
		return nil
	}

	return secondSmallest
}