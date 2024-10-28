
func Minsubarraysum(nums []int) int {
	min := math.MaxInt64
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum < min {
				min = sum
			}
		}
	}
	return min
}

func Minsubarraysum(nums []int) int {
	min := math.MaxInt64
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum < min {
				min = sum
			}
		}
	}
	return min
}

func Minsubarraysum(nums []int) int {
	min := math.MaxInt64
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum < min {
				min = sum
			}
		}
	}
	return min
}

func Minsubarraysum(nums []int) int {
	min := math.MaxInt64
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(