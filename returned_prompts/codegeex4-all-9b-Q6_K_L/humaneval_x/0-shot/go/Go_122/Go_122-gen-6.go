import (
	"strconv"
)

func AddElements(arr []int, k int) int {
	sum := 0
	for i := 0; i < k; i++ {
		if strconv.Itoa(arr[i])[0] == '-' {
			continue
		}
		if len(strconv.Itoa(arr[i])) <= 2 {
			sum += arr[i]
		}
	}
	return sum
}
