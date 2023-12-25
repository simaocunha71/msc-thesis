import (
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {
    return rollmax(numbers, len(numbers))
}

// func rollup(nums []int, i int) func(i int) func() interface{} {
// 	if i == len(nums)-1 {
// 		return nil
// 	} else if nums[i] > nums[i+1] {
// 		var n func() (r int, err error) = func() (r int, err error) {
// 			p := (len(nums)-1)/2 + i // index of max val so far in the sequence
// 			max := nums[i+1] // element at this position
// 			for p > 0 && max == nums[p-1] {
// 				if max == nums[p-1] {
// 					max = nums[p]
// 				} else {
// 					var r [2]*int // rollup function for this position
// 					r.min0 = i+1
// 					r.max0 = len(nums) - 2
// 					max, err = math.MaxInt16(max.MinInt(), r[0]()...)
// 				}
// 				p-- // down one position
// 			} // for p > 0
// 			if max == nums[i+1] {
// 				return
// 			} else {
// 				max = nums[i+1]
// 			}
// 			return n(p