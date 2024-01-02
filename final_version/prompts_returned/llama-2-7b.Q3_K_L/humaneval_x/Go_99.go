import (
    "math"
    "strconv"
    "strings"
)

// Create a function that takes a value (string) representing a number
// and returns the closest integer to it. If the number is equidistant
// from two integers, round it away from zero.
// 
// Examples
// >>> ClosestInteger("10")
// 10
// >>> ClosestInteger("15.3")
// 15
// 
// Note:
// Rounding away from zero means that if the given number is equidistant
// from two integers, the one you should return is the one that is the
// farthest from zero. For example ClosestInteger("14.5") should
// return 15 and ClosestInteger("-14.5") should return -15.
func ClosestInteger(value string) int {
    // split by .
    var (
        nums     []float64
        ints     []int
        temp     float64
        epsilon  = 0.01
        i        int
    )

    if value == "" {
        return 0
    }

    values := strings.Split(value, ".")
    ints = make([]int, len(values))
    for i, v := range values {
        temp, _ := strconv.ParseFloat(v)
        ints[i] = int(temp)
    }

    // parse number as float64
    for _, num := range values {
        nums = append(nums, math.Pow10(math.Exp(math.Log10(float64(i)))))
        i++
    }

    // calculate the difference between each pair of numbers
    for i, v := range values {
        vv := ints[i] - 1
        diff := math.Floor(float64(vv-int(v)) / epsilon) + 1
        if diff > 0 && !(diff > nums[len(nums)-1]) {
            return int(diff)
        } else if !(diff < 2*nums[i] - 1)